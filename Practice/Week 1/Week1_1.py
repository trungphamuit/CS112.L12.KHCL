n = int(input())
l = list (map(int, input().split()))
 
start = 0
end = 0
length = -1
max_end = 0
temp = 0
 
for i in range(n):
  max_end =max_end + l[i] 
 
  if max_end < 0:
    max_end = 0
    temp = i+1
 
  if length < max_end:
    length = max_end
    start = temp 
    end = i 
 
print(start+1,end+1,length)