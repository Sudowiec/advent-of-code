from collections import deque

NUMBER_OF_ELVES = 3017957

left = deque()
right = deque()
for i in range(1, NUMBER_OF_ELVES + 1):
    if i < (NUMBER_OF_ELVES // 2) + 1:
        left.append(i)
    else:
        right.appendleft(i)

while left and right:
    if len(left) > len(right):
        left.pop()
    else:
        right.pop()
    right.appendleft(left.popleft())
    left.append(right.pop())
print(left[0] or right[0])
