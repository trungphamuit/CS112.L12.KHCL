MOD = 1000000007
def multiply(F,M):
  a = (F[0][0] * M[0][0] +  F[0][1] * M[1][0]) % MOD
  b = (F[0][0] * M[0][1] +  F[0][1] * M[1][1]) % MOD
  c = (F[1][0] * M[0][0] +  F[1][1] * M[1][0]) % MOD
  d = (F[1][0] * M[0][1] +  F[1][1] * M[1][1]) % MOD

  F[0][0] = a
  F[0][1] = b
  F[1][0] = c
  F[1][1] = d

def power(F,n):
  if n == 0 or n == 1:
    return
  M = [[1,1],[1,0]]
  power(F, n // 2)  
  multiply(F,F)
  if n % 2 != 0:
    multiply(F,M)

def fibonacci(n):
  F = [[1,1],[1,0]]
  if n == 0:
    return 0
  power(F, n - 1)
  return F[0][0]

n, k = map(int,input().split())
print(n*fibonacci(2*k+1) % MOD)