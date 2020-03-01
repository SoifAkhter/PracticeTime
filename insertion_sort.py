def ins_sort(l):
	for end in range(len(l)):
		pos = end

		while pos > 0 and l[pos]<l[pos-1]:
			l[pos-1], l[pos] = l[pos], l[pos-1]
			pos -= 1

l = [6,98,54,547,2,47,95,83,87,85,120]
ins_sort(l)

print("Sorted List: ",l)