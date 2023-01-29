
"""
data struructed common data structed holo Binneary search

"""
class Node():
    def __init__(self,value):
        self.left=None
        self.Right=None
        self.value=value

    def display(self):
        return self.value

if  __name__ == '__main__':
    root=Node(1)

root.left=Node(2)
root.Right=Node(3)

#
# class BinearyTree():
#     def __init__(self):
#         self.Root=Node(1)

