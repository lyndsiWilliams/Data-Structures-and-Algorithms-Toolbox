'''
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

Access: O(n)
Search: O(n)
Insertion: O(1)
Deletion: O(1)
'''

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        # Return number of elements in the queue
        return self.size

    # Adds an element to the back of the queue
    def enqueue(self, value):
        # Add value to the top of the queue
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    # Removes and returns the element at the front of the queue
    def dequeue(self):
        # Check if queue contains any elements
        if self.size < 0:
            # If so, return element at the top of the queue
            return self.storage.pop()
        # If not, queue is empty so return None
        else:
            return None
        # Set size to storage list length
        self.size = len(self.storage)