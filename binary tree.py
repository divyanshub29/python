'''===Binary Tree==='''

'''A Trre node contains three parts--> data,point to left child,pointer to right child
'''



class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key


#Creating a tree with 4 nodes



root=Node(1)


root.left=Node(2)
root.right=Node(3)


root.left.left=Node(4)
