import itertools

t = 430
k = 8
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
man = []
ans = list(itertools.combinations(ls, k))
for i in ans:
  sumAns = sum(i)
  if sumAns <= t:
    man.append(sumAns)
if man == []:
  print(None)
else:
  print(max(man))
