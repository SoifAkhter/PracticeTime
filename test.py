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

arr =(4,6,7)
print(arr)

lst = [7,8,999,45,34]
print(','.join(lst))

