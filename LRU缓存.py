# https://leetcode.cn/problems/lru-cache/?envType=study-plan-v2&id=mihoyo-2023-spring-sprint]

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
    



class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0


    def get(self, key: int) -> int:
        
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        
        
        
        # move the node to the head of the doublely linked list
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
        
        return node.value



    def put(self, key: int, value: int) -> None:
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            
            self.get(key)
            
            
            
        else:
            new_node = Node(key,value)
        
            # insert the new node into the head
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            
            self.size += 1
            self.key_to_node[key] = new_node
        

        
        if (self.size > self.capacity):
            
            
            # delete the tail node
            
            # first,delete it from the dict
            
            del_node = self.tail.prev
            
            
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size -= 1
            
            del self.key_to_node[del_node.key]
        
        
        
        

        
        
        
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)