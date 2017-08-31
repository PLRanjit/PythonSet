sequence = input("Please enter something: \n")
c = sequence.split(" ")
a = 0
if len(sequence) != 0:
  if (sequence.replace(" ","").isdigit()):
    c = list(map(int, c))
    for i in range(1, max(c)):
      if i not in c:
        a = i
        break;
  else:
    a = 1
else:
  a = 0
print(a)
