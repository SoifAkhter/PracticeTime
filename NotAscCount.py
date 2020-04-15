
def countDesc(lst):
	if len(lst) == 1:
		return 0
	else:
		return int(lst[0]>lst[1]) + countDesc(lst[1:])

lst = [1,2,6,3,1,4]
print(countDesc(lst))