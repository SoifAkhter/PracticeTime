class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if not root:
        print(end=' ')
    elif not root.left and (not root.right):
        print(root.info,end=' ')
        #return [root.info]
    elif root.left and ( not root.right):
        print(root.info, end=' ')
        preOrder(root.left)
        #return [root.info] + preOrder(root.left)
    elif not root.left and root.right:
        print(root.info,end=' ')
        preOrder(root.right)
        #return [root.info] + preOrder(root.right)
    else:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)
        #return [root.info] + preOrder(root.left) + preOrder(root.left)
    



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)