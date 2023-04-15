# https://leetcode.cn/problems/UHnkqh/?envType=study-plan-v2&id=mihoyo-2023-spring-sprint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # store all the vals
        
        vals = []
        
        node = head
        
        while node != None:
            vals.append(node.val)
            node = node.next
            
        vals.reverse()
        
        
        new_head = ListNode()
        old_Node = new_head
        
        
        for val in vals:
            new_Node = ListNode(val)
            old_Node.next = new_Node
            old_Node = new_Node
            
            
        return new_head.next
        
        
        
