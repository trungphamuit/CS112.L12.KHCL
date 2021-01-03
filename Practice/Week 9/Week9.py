n = input()
n2 = int(n)
a = list(map(int, list(n)))
x = [0]*len(a)
ans = []
for i in range(len(a)):
  for j in range(len(x)):
    if i == j:
      x[j] += 0
    else:
      x[j] += a[i]
      x[j] %= 3

for i in range(len(a)):
  temp = a.copy()
  if x[i] == 0:
    temp[i] = 9
    ans.append(temp)
  elif x[i] == 1:
    temp[i] = 8
    ans.append(temp)
  elif x[i] == 2:
    temp[i] = 7
    ans.append(temp)

#print(a,x)
#print(ans)
ans_2 = []
for i in ans:
  ans_2.append(int(''.join([str(x) for x in i])))

ans_2.sort(reverse=True)
if ans_2[0] == n2:
  print(ans_2[0]-3)
else:
  print(ans_2[0])