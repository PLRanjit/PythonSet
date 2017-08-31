import collections

strng = input("Enter the number string without blank spaces\n")  #234561876549 234561356789 44668753
sz =  int(input("Enter the Chunk Size should\n"))
a = []
tot = 0
ans = []
if sz > 0 and len(strng) != 0 and sz < len(strng):
  for i in range(0, len(strng),sz):
    if len(strng[i:i+sz]) == sz:
      a.append(strng[i:i+sz])
  for j in a:
    tot = 0
    for i in j:
      tot = tot + (int(i)**3)
    if tot%2 == 0:
      ans.append(j[::-1])
    else:
      d = collections.deque(list(j))
      d.rotate(-1)
      ans.append("".join(d))
  print("".join(ans))
else:
  print("")

'''
#CodeWars #anter69
 if not s or n < 1 or n > len(s):
        return ""
    
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    print(res)
    
    
 #Codewars #NaMe613, ddwKENwbb
 func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
    print("" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in xrange(0, len(strng) - sz + 1, sz)))
'''
