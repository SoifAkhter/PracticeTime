def sel_sort(l):
	for start in range(len(l)):
		Min = start
		for i in range(start,len(l)):
			if(l[Min]>l[i]):
				Min = i
		(l[start],l[Min]) = (l[Min], l[start])
#li = input("Enter : ")
#print(li)
l=[98, 8, 67, 87, 782,55]
sel_sort(l)
print("Sorted list is : ",l)



