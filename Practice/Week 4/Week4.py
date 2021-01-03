a,k,b,m,n = map(int,input().split())
tree = 0
def day(i):
  break1 = int(i//k)
  break2 = int(i//m)
  tree = a*(i - break1) + b*(i - break2)
  return tree
left = 0
right = n
res = n
while (left <= right):
  mid = (left + right) // 2
  if day(mid) >= n:
    right = mid - 1
    res = mid
  else:
    left = mid + 1
print(res)