import numpy
numbers = input("Enter the number list separeted by blank spcae \neg:1 2 3 4")
n = list(numpy.array(list(map(int, numbers.split(" "))))%2)
print( n.index(1)+1 if n.count(0) > 1 else n.index(0)+1) #to find which one is different from the rest in set

print(list(map(int,"{0:b}".format(int(input("Enter the Number to count the bit in binary"))))).count(1)) #to count the no of 1 in its binary form
