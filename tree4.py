# Tree Min value problem

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

def find_min(node):
    if node is None:
        return float('inf')
    return min(node.value, find_min(node.left), find_min(node.right))

print(find_min(a)) # 3

def find_min_bfs(node):
    if node is None:
        return float('inf')
    
    bfs_queue = Queue()
    bfs_queue.put(node)

    min_value = float('inf')

    while not bfs_queue.empty():
        current = bfs_queue.get()
        min_value = min(min_value, current.value)

        if current.left is not None:
            bfs_queue.put(current.left)
        if current.right is not None:
            bfs_queue.put(current.right)

    return min_value

print(find_min_bfs(a)) # 3