class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        # O(1) → insert at top
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

    def is_empty(self):
        # O(1) -> check if stack is empty
        return self.top is None


def is_valid(expr):
    # O(n) → single pass through string
    st = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        # O(1)
        if ch in "([{":
            st.push(ch)

        # O(1)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False

    # O(1)
    return st.is_empty()

tests = ["()", "([])", "([)]", "{[()]}", "((())", ""]

for t in tests:
    print(t, "->", is_valid(t))