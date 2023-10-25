# Root to leaf path with max sum

from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(10)
b = Node(5)
c = Node(3)
d = Node(4)
e = Node(8)
f = Node(7)
g = Node(9)
h = Node(15)

a.left = b
a.right = h
b.left = c
b.right = e
c.right = d
e.left = f
e.right = g

def find_max_sum(node):
    if node is None:
        return float('-inf')
    
    if node.left is None and node.right is None:
        return node.value
    
    return node.value + max(find_max_sum(node.left), find_max_sum(node.right))

print(find_max_sum(a)) # 31

i = Node(5)
j = Node(11)
k = Node(3)
l = Node(4)
m = Node(2)
n = Node(1)
    
i.left = j
i.right = k
j.left = l
j.right = m
k.right = n

#       5
#      / \
#    11   3
#   / \    \
#  4   2    1

print(find_max_sum(i)) # 20
