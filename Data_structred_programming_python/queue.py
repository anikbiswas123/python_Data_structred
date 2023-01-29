"""
queue means thaat bus truciket counter
queqe follo koro FIFO teacholoy kaj kora thika
"""

from collections import deque

queue=[]

# add item queue

queue.append('a')
queue.append('b')
queue.append('c')

print("Printed the queue")
print(queue)

print("Remove the queue elementd")
print(queue.pop())
print(queue.pop())
print(queue.pop())

print(queue)