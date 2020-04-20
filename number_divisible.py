# Write your code here
def findDiv(n):
    count = 2
    if n == 1:
        return 1
    elif n == 2 or n == 3:
        return 2
    else:
        for i in range(2,n//2 + 1):
            if n % i == 0:
                count +=1
    return count
#
# t = int(input())
# for _ in range(t):
#     print(findDiv(int(input())))
print("Hello Samar!")
