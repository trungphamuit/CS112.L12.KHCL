  l = set()
  for i in range(len(x)-1):
    l.add(x[i:i+2])
  return l

def solve(x,l):
  res = 0
  for i in range(len(x)-1):
    a = x[i:i+2]
    if (a in l):
      res +=1
  return res

string_1 = input().strip()
string_2 = input().strip()
l = sub_string(string_2)
print(solve(string_1,l))