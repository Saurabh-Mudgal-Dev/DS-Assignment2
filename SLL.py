class nodeSLL:
    def __init__(self, data):
        # O(1) → create node
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        # O(1) → initialize head
        self.head = None
    
    def traverse(self):
        # O(n) → visit each node once
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def insert_at_end(self, data):
        # O(n) → traverse to last node
        new_node = nodeSLL(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def insert_at_start(self, data):
        # O(1) → insert at head
        new_node = nodeSLL(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        # O(n) → linear search
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def delete_by_index(self, ind):
        # O(n) → traverse to index
        if not self.head:
            return

        if ind == 0:
            # O(1) → delete head
            self.head = self.head.next
            return

        curr = self.head
        for i in range(ind - 1):
            if not curr.next:
                return
            curr = curr.next

        if curr.next:
            # O(1) → pointer update
            curr.next = curr.next.next
    
    def delete_by_val(self, data):
        # O(n) → search for value
        curr = self.head

        if curr and curr.data == data:
            # O(1) → delete head
            self.head = curr.next
            return

        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next

        if curr:
            # O(1) → pointer update
            prev.next = curr.next


L = [1, 2, 3, 4, 5]
My_List = SLL()

for i in L:
    My_List.insert_at_end(i)

My_List.delete_by_val(2)
My_List.delete_by_index(3)

My_List.traverse()