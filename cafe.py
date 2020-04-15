'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def dis(arr,l):
    lc = 1
    for i in range(l):
        if arr[i]==1:
            c=0
        else:c+=1
    rc=1
    for i in range(l+1,len(arr)):
        if arr[i]==1:
            break
        else:
            rc+=1
    return (lc,rc)
def cafe(n,k):
    arr = [0]*n
   
    for i in range(k):
        if i==0:
            arr[i]=1

        elif i==1:
            arr[i]=1
        else:
            d=[]
            for j in range(n):
                if arr[j] != 1:
                    lc,rc =dis(arr,j)
                    d.append([lc,rc])
                else:
                    d.append([1234567890,1234567890])
            minn= [min(i) for i in d]
            maxx= minn.index(max(minn))
            arr[maxx]=1
    return (d[maxx])




'''test =  int(input())
n,k = map(int,input().split())
for _ in range(tast):
    print(*cafe(n,k))'''

