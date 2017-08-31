customers = []
run = 1
x = input("Enter the array element to break the loop press twice enter key:\n")
while run:
  if x == '':
    break
  customers.append(int(x))
  x = input()
n = int(input("Enter the tills count:\n"))
li = [0]*n
ans = 0
if len(customers) <= n:
  ans = max(customers)
else:
  for i in customers:
    k = li.index(min(li))
    li[k] = li[k] + i
  ans = max(li)
print(ans)
