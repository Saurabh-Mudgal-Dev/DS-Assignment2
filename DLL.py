class Node:
    def __init__(self, data):
        # O(1) → constant time to create a node
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # O(1) → just initializing head pointer
        self.head = None

    def append(self, data):
        # O(n) → traverse entire list to reach last node
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display(self):
        # O(n) → visit each node once for printing
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def insert_after(self, target, x):
        # O(n) → search for target node linearly
        temp = self.head

        while temp:
            if temp.data == target:
                # O(1) → pointer updates once node is found
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next

        print("Target not found")

    def delete_at_position(self, pos):
        # O(n) → traverse to given position
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            # O(1) → deleting head node
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            if not temp:
                return
            temp = temp.next

        if not temp: 
            return

        # O(1) → pointer adjustments after reaching node
        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Initial list:")
dll.display()

dll.insert_after(20, 25)
print("After inserting 25 after 20:")
dll.display()

dll.delete_at_position(2)
print("After deleting position 2:")
dll.display()