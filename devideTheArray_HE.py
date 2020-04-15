# Write your code here

n =  int(input())
A = list(map(int, input().split()))
q = int(input())
d = 1
for _ in range(q):
    d *= int(input())
for i in range(n):
    A[i] //= d

print(*A)
        
