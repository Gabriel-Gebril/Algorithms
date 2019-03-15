# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def intertTree(self, root: TreeNode) -> TreeNode:
        if(root == None):
            return []

        s = root

        t = root.left
        root.left = root.right
        root.right = t

        if (s.left != None):
            Solution.invertTree(self,s.left)

        if(s.right != None):
            Solution.intertTree(self,s.right)

        return s
