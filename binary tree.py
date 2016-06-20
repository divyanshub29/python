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


class BinaryNode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
        
    def add(self,val):
        if val<=self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left=BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right=BinaryNode(val)

    def delete(self):

        if self.left==self.right==None:
            return None
        if self.left==None:
            return self.right
        if self.right==None:
            return self.right

        child = self.left
        grandchild=child.right
        if grandchild:
            while grandchild.right:
                child=grandchild
                grandchild=child.right
            self.value=grandchild.value
            child.right=grandchild.left
        else:
            self.left=child.left
            self.value=child.value

        return self

class BinaryTree:
    def __init__(self):
        #create empty binary tree
        self.root=None

    def add(self,value):
        #insert value into proper location in BT
        if self.root is None:
            self.root=BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self,target):
        #check whether contains target value

        node=self.root
        while node:
            if target==node.value:
                return True

            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self,value):
        #remove value from tree

        if self.root:
            self.root = self.removeFromParent(self.root,value)

    def removeFromParent(self,parent,value):

        if parent is None:
            return None
        if value == parent.value:
            return parent.delete()
        elif value < parent.val:
            parent.left = self.removeFromparent(parent.left,value)

        else:
            parent.right = self.removeFromParent(parent.right,value)
        return parent
        

def balancedTree(a):
    #create balanced BT from orderedvcollection

    bt=BinaryTree()

    addrange(bt,a,0,len(a)-1)

    return bt

def addRange(bt,a,low,high):
    #add range to the bit in way that bt remaibs balanced

    if low <= hihg:
        mid=(low+high)/2

        bt.add(a[mid])
        addRange(bt,a,low,mid-1)
        addRange(bt,a,mid+1,high)











