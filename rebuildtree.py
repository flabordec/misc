# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:35:43 2013

@author: flaborde
"""

def RebuildInPre(inorder, preorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    
    value = preorder.pop(0)
    index = inorder.index(value)    
    lefttree = RebuildInPre(inorder[:index], preorder)
    righttree = RebuildInPre(inorder[index+1:], preorder)
    
    return Node(value, lefttree, righttree)

def RebuildInPost(inorder, postorder):
    if len(postorder) == 0 or len(inorder) == 0:
        return None
        
    value = postorder.pop()
    index = inorder.index(value)
    righttree = RebuildInPost(inorder[index+1:], postorder)
    lefttree = RebuildInPost(inorder[:index], postorder)
    
    return Node(value, lefttree, righttree)

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        
    def SetLeft(self, left):
        self.left = left
        left.parent = self
        
    def SetRight(self, right):
        self.right = right
        right.parent = self

    def StringValue(self, depth = 0):
        value = '{0}{1}'.format(depth * ' ', self.value)
        if self.left != None:
            value += '\n{0}'.format(self.left.StringValue(depth + 1))
        if self.right != None:
            value += '\n{0}'.format(self.right.StringValue(depth + 1))
        
        return value
        
    def __repr__(self):
        return self.StringValue(0)
    
    
if __name__ == '__main__':
    print RebuildInPre('A B C D E F G H I'.split(), 'F B A D C E G I H'.split())
    print "*" * 20
    print RebuildInPost('A B C D E F G H I'.split(), 'A C E D B H I G F'.split())