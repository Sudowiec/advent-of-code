import re
import time
from collections import defaultdict
todo = defaultdict(lambda: [])
points = []
sorted_points = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    match = re.search(r"Step (.) must be finished before step (.) can begin", inp)
    before = match.group(1)
    after = match.group(2)
    points.append(before)
    points.append(after)
    todo[after].append(before)
points = sorted(set(points))
for i in points:
    if i not in todo:
        todo[i] = []

todo_og = todo
print(todo)


step_dur = 0
workers_num = 2
workers = []
for i in range(workers_num):
    workers.append(".")
sec = 0
built = []
working_points = {}
while len(todo) > 0:

    finished_points = []
    for i in working_points:
        if working_points[i] == 0:
            finished_points.append(i)
    finished_points = sorted(finished_points)

    for i in finished_points:
        if i in todo:
            del todo[i]
        built.append(i)
        workers[workers.index(i)] = '.'
        del working_points[i]
        for j in todo:
            if i in todo[j]:
                todo[j].remove(i)

    availble_points = []
    for i in todo:
        if todo[i] == []:
            availble_points.append(i)
    availble_points = sorted(availble_points)

    for i in availble_points:
        if not '.' in workers:
            break
        todo[i] = '-'
        working_points[i] = step_dur + ord(i) - 64
        for j in workers:
            if j == '.':
                workers[workers.index(j)] = i
                break

    print(sec, workers, built)
    # print(todo)

    for i in working_points:
        working_points[i] -= 1
    sec += 1
    # time.sleep(1)
print(sec - 1)