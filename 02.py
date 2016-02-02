#!/usr/bin/python3
print ("hello there")

a,b = 0, 1
if a < b:
    print ('a ({}) is less than b'.format(a,b))
else:
    print ('a({}) is not less than b ({})'.formart(a,b))

#simple fibonacci series

a,b = 0,1
while  b<50:
    print (b)
    a, b = b, a+b
print ("done")

#for loop
#fh = open('lines.txt')
#for line in fh.readlines():
#    print (line)

def isprime(n):
    if n == 1:
        print ("1 is special")
        return False
    for X in range (2, n):
        if n % x == 0:
            print ("{} equals {} x {}".format(n, x, n //x))
            return False
    else:
        print (n, "is a prime number")
        return True

for n in range(1, 20):
    isprime(n)
