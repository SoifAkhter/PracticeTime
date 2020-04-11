def andXorOr(a):
    maxx = a[0]+ a[1]
    m1 = a[0]
    m2 = a[1]
    for i in range(1,len(a)-1):
    	if m2 == a[i+1]:
    		continue
    	elif maxx < m1+a[i+1]:
            m1 = m2
            m2 = a[i+1]
            maxx = m1+m2
    print("Max : {} , m1 : {}, m2 : {}".format(maxx,m1,m2))
    return (((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2))
print("Give Input: ")
a_count = int(input())

a = list(map(int, input().rstrip().split()))    
result = andXorOr(a)
print("result is: ",result)
