#!/usr/bin/python

x = input("Ievadi skaitli: ")


print ("\t%1\t%2\t%3\t%4\t%5")

x1 = x + 10


while x <= x1:
 k = 1
 while k <= 5:
 # print "%d"%(x),
  c = x % k
  print "\t%d" %(c),
  k = k + 1 
 x = x + 1
 print "\n%d" %(x)
print
