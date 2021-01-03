def H_index():
  k = n
  s.sort(reverse=1)
  for i in range(n):
    if s[i] < i + 1:
      k -= 1
  return k

n  = int(input())
s = list(map(int, input().split()))
print(H_index())