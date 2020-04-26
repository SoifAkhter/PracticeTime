def maxSum(n, m, arr): # function definition 
    buff = n//m
    r =n%m
    gr = []
    b = r*(buff+1)
    for i in range(0,b,buff+1):
        gr.append(arr[i:i+buff+1])
    for i in range(b,n, buff):
        gr.append(arr[i:i+buff])
    print(gr) 

    
    
arr =(4,74,87,85,83,89)
print(arr)
lst = [7,34]
print(lst[4])
print("!")

print('#'.join(lst))

