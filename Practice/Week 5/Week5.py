b = input().strip()
a = ''.join(sorted(b,reverse=True))
l1,l2,l0 =[],[],[]

def divide(a,l1,l2,l0):
  Sum = 0
  for i in a:
    if int(i) % 3 == 0:
      l0.append(i)
    elif int(i) % 3 == 2:
      l2.append(i)
    else:
      l1.append(i)
    Sum += int(i)
  return Sum

def remove(Sum_,l1,l2):
  if Sum_ % 3 == 1:
    if l1 == []:
      del l2[-2:]
    else:
      del l1[-1:]
  if Sum_ % 3 == 2:
    if l2  == []:
      del l1[-2:]
    else:
      del l2[-1:]

Sum_ = divide(a,l1,l2,l0)
remove(Sum_,l1,l2)
res = "".join(sorted(l0+l1+l2,reverse=True))
print(res)