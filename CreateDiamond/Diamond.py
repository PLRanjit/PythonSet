n = int(input("Enter the height of diamond and it should be non negative and odd number"))
l = 1
s = ""
if n%2 != 0 and n >= 1:
  for i in range(1,n+1,2):
    for j in range(int(n/2)+2-l,1,-1):
      s = s + " "
    for k in range(0,i):  
      s = s + "*"
    l = l+1
    s = s + "\n"
  l = 1
  for i in range(n-2,0,-2):
    for j in range(0,l):
      s = s + " "
    for k in range(0,i):  
      s = s + "*"
      sys.stdout.softspace=False;
    s = s + "\n"
    l = l + 1
  print(s)
  
  
  '''
  #Codewars #Krernertok, Imanflow, Cod3r, Lukegb94
      if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None
        
   #Codewar #Evgen123
       if n % 2 == 0 or n < 1: return None
    d = [' ' * ((n-i)/2) + '*' * i for i in xrange(1, n, 2)]
    d.extend([' ' * ((n-i)/2) + '*' * i for i in xrange(n, 0, -2)])
    return '\n'.join(d) + '\n'
  '''
