n = int(input())
res = 0
x = int(n / 3)
y = n % 3
if y == 0:
  res += x*7
elif y == 1:
  res += (x-1)*7 + 4
elif y == 2:
  res += x*7 + 1
print(res)