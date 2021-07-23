import re
from collections import defaultdict
last_guard = -1
last_sleep = -1
guards_sum = defaultdict(lambda: 0)
slept_minutes = {}
while True:
    try:
        inp = input()
    except EOFError:
        break
    inp = re.search(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.+)", inp)
    msg = inp.group(6)
    minute = int(inp.group(5))
    if msg[0] == "G":
        match = re.search(r"Guard #(\d+) begins shift", msg)
        last_guard = int(match.group(1))
    if msg[0] == "f":
        last_sleep = minute
    if msg[0] == "w":
        sleep_time = minute - last_sleep
        guards_sum[last_guard] += sleep_time
        sleep_list = range(last_sleep, minute)
        if last_guard not in slept_minutes:
            slept_minutes[last_guard] = defaultdict(lambda: 0)
        for i in sleep_list:
            slept_minutes[last_guard][i] += 1




maxguard = 0
maxval = 0
for i in guards_sum:
    if guards_sum[i] > maxval:
        maxval = guards_sum[i]
        maxguard = i
print(maxguard)

maxminute = 0
maxval = 0
for i in slept_minutes[maxguard]:
    if slept_minutes[maxguard][i] > maxval:
        maxval = slept_minutes[maxguard][i]
        maxminute = i
print(maxminute)
print(maxminute * maxguard)

maxerminute = 0
maxval = 0
maxerguard = 0
for i in slept_minutes:
    for j in slept_minutes[i]:
        if slept_minutes[i][j] > maxval:
            maxval = slept_minutes[i][j]
            maxerguard = i
            maxerminute = j
print(maxerminute)
print(maxerguard)
print(maxerminute * maxerguard)
