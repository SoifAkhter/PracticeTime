def sel_sort(l):
	for start in range(len(l)):
		Min = start
		for i in range(start,len(l)):
			if(l[Min]>l[i]):
				Min = i
		(l[start],l[Min]) = (l[Min], l[start])
#l = list(map(int, input("Enter the List: ").split()))
#el_sort(l)
l=input("num: ")
print("Sorted list is : ",l)













