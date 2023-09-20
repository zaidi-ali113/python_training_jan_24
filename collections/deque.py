from collections import deque

# Create a deque
queue = deque()

# Enqueue items (add to the right)
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

# Dequeue items (remove from the left)
item = queue.popleft()  # Removes "Alice"

x=1