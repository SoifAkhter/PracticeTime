def ins_sort(l):
	for end in range(len(l)):
		pos = end

		while pos > 0 and l[pos]<l[pos-1]:
			l[pos-1], l[pos] = l[pos], l[pos-1]
			pos -= 1

l = [5,3,43,7,97,4,656,54]
ins_sort(l)

print("Sorted List: ",l)