def rec_ins(l):
	isort(l,len(l))

def isort(seq,k):

	if k>1:
		isort(seq,k-1)
		insert(seq,k-1)

def insert(seq,k):
	pos=k
	while pos>0 and seq[pos]<seq[pos-1]:
		(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
		pos -= 1

l=[21,454,566,76,546]
rec_ins(l)
print("Sorted List : ",l)
