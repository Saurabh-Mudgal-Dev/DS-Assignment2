# Data Structures Lab Work (ETCCDS202)

**Name:** Saurabh 
**Course:** Data Structures Lab  
**Program:** B.Tech Computer Science  
**Section:** A  

---

## About This Repository

This repository documents practical implementations developed as part of the Data Structures Lab coursework (2026). The focus is on building core linear data structures from scratch to understand their internal mechanics, efficiency, and real-world usage.

Rather than relying on built-in abstractions, each structure is implemented manually to emphasize pointer handling, memory behavior, and algorithmic thinking.

---

## Covered Concepts (Unit 2)

### 🔹 Linked Lists
- Implementation of **Singly Linked List (SLL)** and **Doubly Linked List (DLL)**
- Supports operations like insertion (start/end/middle) and deletion
- Proper handling of edge cases such as empty list and head/tail updates

### 🔹 Stack (Linked List Based)
- Stack built using SLL with top pointer
- Efficient **push, pop, peek** operations
- All operations designed to run in constant time

### 🔹 Queue (Linked List Based)
- Queue implemented with **head and tail pointers**
- Ensures **O(1) enqueue and dequeue**
- Demonstrates FIFO behavior clearly

### 🔹 Parentheses Validation
- Uses stack logic to verify balanced brackets
- Handles multiple types: `()`, `{}`, `[]`
- Useful for parsing expressions and syntax validation

### 🔹 Dynamic Array (Custom Implementation)
- Simulates behavior similar to Python lists
- Includes:
  - Automatic resizing (capacity doubling)
  - Append and pop operations
- Highlights **amortized time complexity**

---

## Tech Details

- **Language Used:** Python 3  
- **Libraries:** Standard Library (`ctypes` for low-level array simulation)  
- **Execution Mode:** Command line / terminal  

---

## Learning Focus

- Understanding **time complexity trade-offs**
- Manual handling of **memory-like structures**
- Translating theoretical DS concepts into working code
- Recognizing when and why certain structures are preferred

---

## How to Run

1. Clone the repository  
2. Navigate to the desired file  
3. Run using:
   ```bash
   python filename.py