class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        # O(1) → insert at head (top)
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # O(1) → remove top element
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        # O(1) → return top without removing
        if not self.top:
            return None
        return self.top.data

    def is_empty(self):
        # O(1) → check if stack is empty
        return self.top is None

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())

print("Popped:", s.pop())
print("Top after pop:", s.peek())

print("Is empty:", s.is_empty())

s.pop()
s.pop()

print("Is empty after removing all:", s.is_empty())