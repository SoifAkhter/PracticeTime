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

    
    
arr =(4,7,9,89)
print(arr)
lst = [7,34]
print(lst)

print(','.join(lst))

