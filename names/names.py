import time

class Stack:
    def __init__(self):
        self.storage = list()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
       
        if value < self.value:
            if self.left == None:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.value == None:
            return None
        else:
            if self.right == None:
                return self.value
            else:
                return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left != None:
            self.left.for_each(fn)

        if self.right != None:
            self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self is None:
            return
        

        if self.left != None:
            self.left.in_order_print()
            
        print(self.value)

        if self.right != None:
            self.right.in_order_print()
            
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
""" for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1) """
            


bst = BSTNode("")

for name_2 in names_2:
    bst.insert(name_2)

for name_1 in names_1:
    if bst.contains(name_1):
        duplicates.append(name_1)





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
