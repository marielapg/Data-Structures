"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else: 
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
         else:
            return self.value

    def iterative_get_max(self):
        current _max = self.value
        current  = self
        while current is not None:
            if current.value > current.max:
                current_max = current_value
            current = current.right 
        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


    def iterative_for_each(self, fn):
        stack = [] 
        stack.append(self) 
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            fn(current.value)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        storage = Stack()
        storage.push(node)
        while storage.len() > 0:
            head = storage.pop()
            if head.left:
                self.in_order_print(head.left)
            if head.right:
                storage.push(head.right)
            print(head.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.enqueue(node)
        while storage.len() > 0:
            head = storage.dequeue()
            print(head.value)
            if head.left:
                storage.enqueue(head.left)
            if head.right:
                storage.enqueue(head.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)
        while storage.len() > 0:
            head = storage.pop()
            print(head.value)
            if head.left:
                storage.push(head.left)
            if head.right:
                storage.push(head.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
