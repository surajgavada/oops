class Queue:
    def __init__(self):
        # Initialize an empty storage list
        self.items = []

    def enqueue(self, item=None):
        if item is not None:
            self.items.append(item)
            print(f"Enqueued: '{item}'")
        else:
            print("enqueue() called without an argument. No item added.")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: '{removed}'")
            return removed
        print("Cannot dequeue: Queue is empty.")
        return None

    def peek(self):
        if not self.is_empty():
            front = self.items[0]
            print(f"Peek (front item): '{front}'")
            return front
        print("Cannot peek: Queue is empty.")
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(f"Current Cqueue: {self.items}\n")


# -------------------------------------------------------------
# Performing the Operations
# -------------------------------------------------------------

# 1. Empty queue named Cqueue
print("1. Initializing empty queue:")
Cqueue = Queue()
Cqueue.display()

# 2. Enqueue A
print("2. Enqueue 'A':")
Cqueue.enqueue("A")
Cqueue.display()

# 3. Enqueue B
print("3. Enqueue 'B':")
Cqueue.enqueue("B")
Cqueue.display()

# 4. is_empty() check
print("4. Checking if Cqueue is empty:")
print(f"is_empty() result: {Cqueue.is_empty()}")
Cqueue.display()

# 5. enqueue() with no argument
print("5. Calling enqueue() without an item:")
Cqueue.enqueue()
Cqueue.display()

# 6. peek()
print("6. Peek at front element:")
Cqueue.peek()
Cqueue.display()

# 7. dequeue()
print("7. Dequeue front element:")
Cqueue.dequeue()
Cqueue.display()