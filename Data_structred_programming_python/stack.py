from os import remove


# class stack():
#     def __init__(self):
#         self.list=[]
#
#     def push(self,val):
#         self.list.append(val)
#
#     def pop(self):
#         return self.list.pop()
#
#     def  display(self):
#         return self.list
#
# mystack=stack()
# mystack.push(1)
# mystack.push(2)
# mystack.push(3)
# mystack.push(4)
# print(mystack.display())
# mystack.pop()
# mystack.pop()
# print(mystack.display())

# class  stack():
#     def __init__(self):
#         self.list=[]
#
#     def push(self,val):
#         self.list.append(val)
#
#     def pop(self):
#          self.list.pop()
#
#     def display(self):
#         return self.list
#
# stack=stack()
# stack.push(2)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# print(stack.display())
#
# stack.pop()
# stack.pop()
# print(stack.display())


# Python program to demonstrate
# stack implementation using a linked list.
"""
 stack follow kora LIFO meanns last in fast out
 lifo methodlogoy teachnology follow kora 
 
"""
# node class

# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
#
#
# class Stack:
#
# 	# Initializing a stack.
# 	# Use a dummy node, which is
# 	# easier for handling edge cases.
# 	def __init__(self):
# 		self.head = Node("head")
# 		self.size = 0
#
# 	# String representation of the stack
# 	def __str__(self):
# 		cur = self.head.next
# 		out = ""
# 		while cur:
# 			out += str(cur.value) + "->"
# 			cur = cur.next
# 		return out[:-3]
#
# 	# Get the current size of the stack
# 	def getSize(self):
# 		return self.size
#
# 	# Check if the stack is empty
# 	def isEmpty(self):
# 		return self.size == 0
#
# 	# Get the top item of the stack
# 	def peek(self):
#
# 		# Sanitary check to see if we
# 		# are peeking an empty stack.
# 		if self.isEmpty():
# 			raise Exception("Peeking from an empty stack")
# 		return self.head.next.value
#
# 	# Push a value into the stack.
# 	def push(self, value):
# 		node = Node(value)
# 		node.next = self.head.next
# 		self.head.next = node
# 		self.size += 1
#
# 	# Remove a value from the stack and return.
# 	def pop(self):
# 		if self.isEmpty():
# 			raise Exception("Popping from an empty stack")
# 		remove = self.head.next
# 		self.head.next = self.head.next.next
# 		self.size -= 1
# 		return remove.value
#
#
# # Driver Code
# if __name__ == "__main__":
# 	stack = Stack()
# 	for i in range(1, 11):
# 		stack.push(i)
# 	print(f"Stack: {stack}")
#
# 	for j in range(1, 6):
# 		remove = stack.pop()
# 		print(f"Pop: {remove}")
# 	print(f"Stack: {stack}")
#
#

# Python program to demonstrate
# stack implementation using a linked list.
# node class

# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
#
#
# class Stack:
#
# 	# Initializing a stack.
# 	# Use a dummy node, which is
# 	# easier for handling edge cases.
# 	def __init__(self):
# 		self.head = Node("head")
# 		self.size = 0
#
# 	# String representation of the stack
# 	def __str__(self):
# 		cur = self.head.next
# 		out = ""
# 		while cur:
# 			out += str(cur.value) + "->"
# 			cur = cur.next
# 		return out[:-3]
#
# 	# Get the current size of the stack
# 	def getSize(self):
# 		return self.size
#
# 	# Check if the stack is empty
# 	def isEmpty(self):
# 		return self.size == 0
#
# 	# Get the top item of the stack
# 	def peek(self):
#
# 		# Sanitary check to see if we
# 		# are peeking an empty stack.
# 		if self.isEmpty():
# 			raise Exception("Peeking from an empty stack")
# 		return self.head.next.value
#
# 	# Push a value into the stack.
# 	def push(self, value):
# 		node = Node(value)
# 		node.next = self.head.next
# 		self.head.next = node
# 		self.size += 1
#
# 	# Remove a value from the stack and return.
# 	def pop(self):
# 		if self.isEmpty():
# 			raise Exception("Popping from an empty stack")
# 		remove = self.head.next
# 		self.head.next = self.head.next.next
# 		self.size -= 1
# 		return remove.value
#
#
# # Driver Code
# if __name__ == "__main__":
# 	stack = Stack()
# 	for i in range(1, 11):
# 		stack.push(i)
# 	print(f"Stack: {stack}")
# 	print(stack.peek())
#
# 	for _ in range(1, 6):
# 		remove = stack.pop()
# 		print(f"Pop: {remove}")
# 	print(f"Stack: {stack}")


# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class Stack():
#
#     def __init__(self):
#         self.head = Node("head")
#         self.size = 0
#
#     # String representation of the stack
#     def __str__(self):
#         cur = self.head.next
#         out = ""
#         while cur:
#             out += str(cur.value) + "->"
#             cur = cur.next
#         return out[:-3]
#
#     # stack get currents size
#     def getSize(self):
#         return self.size
#
#     # check stack isemty kina
#
#     def ismpity(self):
#         return self.size == 0
#
#     def peeks(self):
#         if self.ismpity():
#             raise Exception('peeking the stack emty!')
#         return self.head.next.value
#
#     # Push a value into the stack.
#     def push(self, value):
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1
#
#     # Remove a value from the stack and return.
#     def pop(self):
#         if self.ismpity():
#             raise Exception("Popping from an empty stack")
#         remove = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return remove.value
#
#
# mystack = Stack()
# for i in range(1,10):
#     mystack.push(i)
# print(mystack)
# print(mystack.peeks())
# for i in range(1,6):
#     mystack.pop()
# print(mystack)
# print(mystack.peeks())


class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class stack():
    def __init__(self):
        self.head=Node('head')
        self.size=0

 # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def getsize(self):
        return self.size

    def isempty(self):
        return  self.size == 0

    def push(self,value):
        node=Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    def peeks(self):
        if self.isempty():
            raise Exception("Peeking from an stack empty !")
        return self.head.next.value


    def pop(self):

        if self.isempty():
            raise Exception("Stack is empty!")
        remove=self.head.next
        self.head.next=self.head.next.next
        self.size -=1
        return remove.value


if __name__ == '__main__':
    stack=stack()
    for i in range(1,10):
        stack.push(i)

    print(stack)
    print(stack.peeks())

    for i in range(1,4):
        stack.pop()

    print(stack)
    print(stack.peeks())



