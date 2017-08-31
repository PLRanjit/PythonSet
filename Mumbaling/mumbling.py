s = "ZpglnRxqenU"
a = list(s)
m = ""
j = 0
for i in a:
  m = m + i.upper()
  for x in range(0, j):
    m = m + i.lower()
  m = m + "-"
  j = j + 1
m = m[:-1]
print(m)
