# A stack is a data structure whose primary purpose is to store and
# return elements in Last In First Out order. 

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # Return number of elements in the stack
        return self.size

    def push(self, value):
        # Add value to the top of the stack
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

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