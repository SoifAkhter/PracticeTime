class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val): 
        #Enter you code here.
        temp = Node(val)
        if not self.root:
            self.root = temp
        else: 
            cur = self.root
            while True:
                if cur.info > val:
                    if not cur.left:
                        cur.left = temp
                        return self.root
                    else:
                        cur = cur.left
                elif cur.info < val:
                    if  not cur.right:
                        cur.right = temp
                        return self.root
                    else:
                        cur = cur.right

                    




            

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
