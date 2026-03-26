class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        # O(1) → insert at tail using tail pointer
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # O(1) → remove from head
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            # O(1) → reset tail when queue becomes empty
            self.tail = None
        return val

    def front(self):
        # O(1) → access front element
        if not self.head:
            return None
        return self.head.data

    def display(self):
        # O(n) → traverse entire queue
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())

print("Dequeued:", q.dequeue())
print("Front:", q.front())

q.enqueue(40)
q.enqueue(50)

print("Dequeued:", q.dequeue())

print("Final Queue:")
q.display()