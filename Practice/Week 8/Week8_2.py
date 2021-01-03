from sys import stdin,stdout
s = stdin.readline().strip()
n = int(stdin.readline())

String = {}
for i in range(97, 123):
    String[chr(i)] = 2**(i-97)

Count = []
for i in range(len(s)+1):
  Count.append(0)

for i in range(len(s)):
    Count[i+1] = Count[i] + String[s[i]]

for i in range(n):
  a, b, c, d = map(int, stdin.readline().strip().split(' '))
  if Count[b] - Count[a-1] == Count[d] - Count[c-1]:
    print("YES")
  else:
    print("NO")