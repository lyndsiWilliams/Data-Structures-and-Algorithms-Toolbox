'''
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

Access: O(n)
Search: O(n)
Insertion: O(1)
Deletion: O(1)
'''

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # Return number of elements in the stack
        return self.size

    # Adds an element to the back of the stack
    def push(self, value):
        # Add value to the top of the stack
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    # Removes and returns the element at the front of the stack
    def pop(self):
        # Check if stack contains any elements
        if self.size < 0:
            # If so, return element at the top of the stack
            return self.storage.pop()
        # If not, stack is empty so return None
        else:
            return None
        # Set size to storage list length
        self.size = len(self.storage)