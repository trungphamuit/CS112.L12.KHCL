import sys 
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0

while a*d <= b*c:
    a,b = a+1,b+1
    g = math.gcd(a, b)
    a,b = a//g, b//g
    count += 1
    if a == c and b == d:
      print(count)
      sys.exit()

print(0)