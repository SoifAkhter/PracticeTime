# Write your code here

t = int(input())
for _ in range(t):
    x = int(input())
    l1 = x//4
    l2 = l1
    r = x % 4
    if (r>=2):
        l2 = l2 + 1
    print(l1*l2)