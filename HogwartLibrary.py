
lst = []
while True:
    lst.append(input())
    if lst[-1] == 'EndOfInput':
        break

bindex = lst.index("Books")
brindex = lst.index("Borrowers")
ckindex = lst.index("Checkouts")
books = {}
borrower = {}
checkout = {}
for bk in lst[bindex+1:brindex]:
    buff = bk.split('~')
    books[buff[0]] = buff[1]
for br in lst[brindex+1:ckindex]:
    buff = br.split('~')
    borrower[buff[0]] = buff[1]
for ck in lst[ckindex+1:-1]:
    buff = ck.split('~')
    checkout[buff[1]] = [buff[0],buff[2]]
print(books)
print(borrower)
print(checkout)

result = []

for i,j in checkout.items():
    result.append('~'.join([j[1],borrower[j[0]],i,books[i]]))
result.sort()
print(*result, sep="\n")



