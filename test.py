def maxSum(n, m, arr): # function definition 
    buff = n//m
    r = n % m
    gr = []
    b = r*(buff+1)
    for i in range(0,b,buff+1):
        gr.append(arr[i:i+buff+1])
    for i in range(b,n, buff):
        gr.append(arr[i:i+buff])
    print(gr) 

    
    
arr =(4,85,83,5,90)
print(arr)
lst = [7,3,4]
print(lst[4])
print("Hello! I'm Soif.")
print("One and only")
print("AI with Deep Learning")

print(''.join(lst))

