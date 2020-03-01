def merge(A, B):
	C,m,n = [],len(A),len(B)
	i,j = 0,0
	while i+j<m+n:
		if i==m:
			C.append(B[j])
			j += 1
		elif j==n:
			C.append(A[i])
			i+=1
		elif A[i]<=B[j]:
			C.append(A[i])
			i+=1
		elif A[i]>B[j]:
			C.append(B[j])
			j+=1
	return C

def merge_sort(X,left,right):
	if right - left<=1:
		return X[left:right]
	if right - left > 1:
		mid = (left+right)//2
		L = merge_sort(X,left,mid)
		R = merge_sort(X,mid,right)
		return merge(L,R)

lst = [48,56,76,5,6,24,546]
print("Sorted List: ",merge_sort(lst,0,len(lst)))