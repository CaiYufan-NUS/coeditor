class Node:
    def __init__(self, data, head):
        self.item = data
        self.next = head
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.size

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(3)
linked_list.add(5)
linked_list.remove()
# check the number
assert len(linked_list) == 2
assert linked_list.len() == 2
