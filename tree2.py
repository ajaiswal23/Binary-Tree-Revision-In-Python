# Tree includes problem
from queue import Queue
from queue import LifoQueue as Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       a
#      / \
#     b   c
#   / \    \
#  d   e    f

def find_bfs(node, target):
    bfs_queue = Queue()
    if node is None:
        return
    
    bfs_queue.put(node)

    while not bfs_queue.empty():
        current = bfs_queue.get()
        if current.value == target:
            return True
        
        if current.left is not None:
            bfs_queue.put(current.left)
        if current.right is not None:
            bfs_queue.put(current.right)

    return False

def find_dfs(node, target):
    dfs_stack = Stack()
    if node is None:
        return
    
    dfs_stack.put(node)

    while not dfs_stack.empty():
        current = dfs_stack.get()
        if current.value == target:
            return True
        
        if current.left is not None:
            dfs_stack.put(current.left)
        if current.right is not None:
            dfs_stack.put(current.right)

    return False

if find_bfs(a, "E"): # True
    print("E is in the tree")
else:
    print("E is not in the tree")

if find_dfs(a, "Z"): # True
    print("Z is in the tree")
else:
    print("Z is not in the tree")

if find_bfs(a, "D"): # False
    print("D is in the tree")
else:
    print("D is not in the tree")

if find_dfs(a, "Z"): # False
    print("Z is in the tree")
else:
    print("Z is not in the tree")