""" Node is defined as follow: 
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import sys
sys.setrecursionlimit(100000)
def check_binary_search_tree_(root):
    if not root.left and not root.right:
        return 1
    elif root.left and not root.right:
        if root.left.data < root.data :
            return check_binary_search_tree_(root.left)
        else:
            return 0
    elif not root.left and root.right:
        if root.right.data > root.data:
            return check_binary_search_tree_(root.right)
        else:
            return 0
    else:
        if root.left.data < root.data and root.right.data > root.data:
            return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)
        else:
            return 0
            
