def quick_sort(A,l,r):
	if r-l <= 1:
		return
	yellow = l+1
	for green in range(l+1,r):
		if A[green] <= A[l]:
			(A[yellow],A[green]) = (A[green],A[yellow])
			yellow += 1
	(A[l],A[yellow-1]) = (A[yellow-1],A[l])
	quick_sort(A,l,yellow-1)
	quick_sort(A,yellow,r)

lst = [743,546,657,7,7,4,56,65,657,6,6,77,87878,3,2345,455,66,773,75]
quick_sort(lst,0,len(lst))
print("Sorted List: ",lst)
