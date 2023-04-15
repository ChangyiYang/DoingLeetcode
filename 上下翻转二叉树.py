# https://leetcode.cn/problems/binary-tree-upside-down/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def upsideDown(root):
            if root.left == None or root.right == None:
                return
            
            left = root.left
            right = root.right

            left_left = left.left

            left.right = root
            left.left = right

            return left_left

        while(root != None):
            root = upsideDown(root)



        



