def maxSum(n, m, arr):
    buff = n//m
    r =n%m
    gr = []
    b = r*(buff+1)
    for i in range(0,b,buff+1):
        gr.append(arr[i:i+buff+1])
    for i in range(b,n, buff):
        gr.append(arr[i:i+buff])
    print(gr) 

arr = [300,405,506,21,45,765,2352,65]
arr.sort()
print(arr)

