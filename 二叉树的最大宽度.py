# https://leetcode.cn/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        
        # try: doing a BFS
        
        from collections import defaultdict
        
        width_dict = defaultdict(lambda : (float('inf'),float('-inf')))
        
        import heapq
        
        pq = []
        
        
        heapq.heappush(pq, (0, 1,root))
        
        depth = 0
        while pq:
            depth, width ,node = heapq.heappop(pq)
            
            width_dict[depth] = (min(width_dict[depth][0], width), max(width_dict[depth][1], width))
            
            if node.left != None:
                heapq.heappush(pq, (depth +1, 2*width, node.left))
            
            if node.right != None:
                heapq.heappush(pq, (depth + 1, 2*width +1 ,node.right))
            
        
        max_width = 0
        for value in width_dict.values():
            
            max_width = max(max_width, value[1]- value[0])
            
        return max_width
            
            
            
            
        


                
            
        
        
        
        