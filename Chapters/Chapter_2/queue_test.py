from collections import deque

queue = deque()

for i in range(10):
    queue.append(i+1)

print(queue)

queue.popleft()
queue.popleft()

print(queue)

queue.append(11)

print(queue)
print(queue[0])