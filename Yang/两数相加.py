# https://leetcode.cn/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        # 进位的数
        z = 0
        x = (l1.val + l2.val)//10
        # 留下的数
        y = l1.val + l2.val - x*10
        
        z = x
        
        old_node = ListNode(y)
        
        result = old_node
        
        l1 = l1.next
        l2 = l2.next
        
        while l1!= None and l2 != None:
            
            # 进位的数
            x = (l1.val + l2.val + z)//10
            # 留下的数
            y = l1.val + l2.val + z - x*10
            # 进位的数
            z = x
            
            new_node = ListNode(y)
            old_node.next = new_node
            old_node = new_node
            
            l1 = l1.next
            l2 = l2.next
            
        while l1!= None:
            # 进位的数
            x = (l1.val + z)//10
            # 留下的数
            y = l1.val + z - x*10
            # 进位的数
            z = x
            
            new_node = ListNode(y)
            old_node.next = new_node
            old_node = new_node
            
            l1 = l1.next
            
        while l2!= None:
            # 进位的数
            x = (l2.val + z)//10
            # 留下的数
            y = l2.val + z - x*10
            # 进位的数
            z = x
            
            new_node = ListNode(y)
            old_node.next = new_node
            old_node = new_node
            
            l2 = l2.next
            
        if (z != 0):
            new_node = ListNode(z)
            old_node.next = new_node
            
        return result
            
            
            
            