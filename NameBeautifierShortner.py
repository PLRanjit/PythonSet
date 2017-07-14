t = int(input())
name = ""
for i in range(0,t):
  s = input().title()
  s = s.split(" ")
  n = s[-1:]
  for i in n:
    s.remove(i)
  for j in s:
    name = name + j[:1]+". "
  for i in n:
    name = name + i
  print(name)
  name = ""
