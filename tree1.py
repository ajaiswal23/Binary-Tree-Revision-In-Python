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

# Breadth First Traversals:
def bfs(node):
    bfs_queue = Queue()
    bfs_array = []
    if node is None:
        return
    
    bfs_queue.put(node)

    while not bfs_queue.empty():
        current = bfs_queue.get()
        bfs_array.append(current.value)
        
        if current.left is not None:
            bfs_queue.put(current.left)
        if current.right is not None:
            bfs_queue.put(current.right)

    return bfs_array
        

breadth_traversal = bfs(a) # ['A', 'B', 'C', 'D', 'E', 'F']
# print(breadth_traversal)

# Depth First Traversals:

# 1. Preorder Traversal:
def dfs_pre(node):
    dfs_array = []
    dfs_stack = Stack()
    if node is None:
        return
    
    dfs_stack.put(node)
    
    while not dfs_stack.empty():
        current = dfs_stack.get()
        dfs_array.append(current.value)

        if current.right is not None:
            dfs_stack.put(current.right)
        if current.left is not None:
            dfs_stack.put(current.left)

    return dfs_array

preorder_traversal = dfs_pre(a) # ['A', 'B', 'D', 'E', 'C', 'F']
print("Preorder Traversal using stack:",preorder_traversal)

def dfs_pre_recursive(node, dfs_array):
    if node is None:
        return
    dfs_array.append(node.value)
    dfs_pre_recursive(node.left, dfs_array)
    dfs_pre_recursive(node.right, dfs_array)
    return dfs_array

preorder_traversal_recursive = dfs_pre_recursive(a, []) # ['A', 'B', 'D', 'E', 'C', 'F']
print("Preorder Traversal using recursion:",preorder_traversal_recursive)

# 2. Postorder Traversal:

def dfs_post(node):
    dfs_array = []
    dfs_stack = Stack()
    if node is None:
        return
    
    dfs_stack.put(node)

    while not dfs_stack.empty():
        current = dfs_stack.get()
        dfs_array.append(current.value)

        if current.left is not None:
            dfs_stack.put(current.left)
        if current.right is not None:
            dfs_stack.put(current.right)

    return dfs_array[::-1]

postorder_traversal = dfs_post(a) # ['D', 'E', 'B', 'F', 'C', 'A']
print("Postorder Traversal using stack:",postorder_traversal)

def dfs_post_recursive(node, dfs_array):
    if node is None:
        return
    dfs_post_recursive(node.left, dfs_array)
    dfs_post_recursive(node.right, dfs_array)
    dfs_array.append(node.value)
    return dfs_array

postorder_traversal_recursive = dfs_post_recursive(a, []) # ['D', 'E', 'B', 'F', 'C', 'A']
print("Postorder Traversal using recursion:",postorder_traversal_recursive)

# 3. Inorder Traversal:

def dfs_in_recursive(node, dfs_array):
    if node is None:
        return
    dfs_in_recursive(node.left, dfs_array)
    dfs_array.append(node.value)
    dfs_in_recursive(node.right, dfs_array)
    return dfs_array

inorder_traversal_recursive = dfs_in_recursive(a, []) # ['D', 'B', 'E', 'A', 'C', 'F']
print("Inorder Traversal using recursion:",inorder_traversal_recursive)
    