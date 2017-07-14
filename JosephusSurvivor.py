from collections import deque
n = int(input())
k = int(input()) - 1
c = list(range(1,n+1))
items = deque(c)
while len(items) != 1:
  items.rotate(-k)
  items.popleft()

for i in items:
  print(i)
