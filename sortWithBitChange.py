def bitDiff(x,y):
	if x //1000 == y//1000:
		if x//100 == y//100:
			if x//10 == y//10:
				return 0
			return 1
		return 2
	return 3

def bitSort(lst):
	for x in range(len(lst)):
		if x==0:
			lst[x] = lst[x] % 1000 +1000
		else:
			p = bitDiff(lst[x-1],lst[x])
			f = 0
			for i in range(p,4):
				if f == 1:
					break
				m = (lst[x-1]%10**(i+1))//10**i
				for j in range(m,10):
					if lst[x-1] % 10**(i+1) < lst[x] % 10**i + j*10**i:
						lst[x] = (lst[x]//10**(i+1))*10**(i+1) +j*10**i + lst[x] % 10**i
						f = 1
						break


arr = [5244,1223,3221,1113,1143]
bitSort(arr)
print(arr)