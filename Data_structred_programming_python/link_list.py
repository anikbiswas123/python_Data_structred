# class Node():
#     def __init__(self,value):
#         self.next=None
#         self.pre= None
#         self.value=value
#
# class Double_lik_list():
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size = 0
#
#     def add (self,val):
#         node = Node(val)
#         if self.tail is None:
#             self.head = node
#             self.tail = node
#             self.size += 1
#         else:
#             self.tail.next = node
#             node.pre = self.head
#             self.tail = node
#             self.size += 1
#
#     def __str__(self):
#         vals=[]
#         node=self.head
#         while node is not None:
#               vals.append(node.value)
#               node = node.next
#
#         return  f"[{' , '.join(str(val) for val in  vals)}]"
#
# mylist=Double_lik_list()
# mylist.add(1)
# mylist.add(5)
# mylist.add(2)
#
# print(mylist)


class Node():
    def __init__(self,val):
        self.next=None
        self.pre=None
        self.valus=val

class Doublelink_list():

    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0

    def add(self,val):
        node=Node(val)
        if self.tail is None:
            self.head= node
            self.tail= node
            self.size += 1
        else:
            self.tail.next = node
            # node.pre = self.head
            node.pre = self.tail
            self.tail = node
            self.size += 1


    def remove_node(self,node):
        if node.pre is None:
            node.pre=node.next
        else:
            node.pre.next = node.next

        if node.next is None:
            self.tail=node.pre
        else:
            node.next.pre = node.pre
        # node.pre.next=node.next
        # node.next.pre =node.pre
        self.size -=1


    def remove(self,vale):
        node=self.head
        while node is not  None:
            if node.valus == vale:
                self.remove_node(node)
                break
            node =node.next

    def remove_last(self):
        if self.tail is not None:
            self.remove_node(self.tail)

    def font(self):
        return self.head.val


    def back(self):
        return self.tail.val





    def __str__(self):
        vals=[]
        node=self.head
        while node is not  None:
            vals.append(node.valus)
            node=node.next

        return f"[{', '.join(str(val)for val in vals)}]"

mylist=Doublelink_list()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
print(mylist)
mylist.remove(3)
print(mylist)
mylist.remove_last()
print(mylist)




