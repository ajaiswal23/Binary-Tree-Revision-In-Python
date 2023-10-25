# Tree sum problem

from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def find_sum(node):
    if node is None:
        return 0
    return node.value + find_sum(node.left) + find_sum(node.right)

print(find_sum(a)) # 21

def find_sum_bfs(node):
    if node is None:
        return 0
    
    bfs_queue = Queue()
    bfs_queue.put(node)

    sum = 0

    while not bfs_queue.empty():
        current = bfs_queue.get()
        sum += current.value

        if current.left is not None:
            bfs_queue.put(current.left)
        if current.right is not None:
            bfs_queue.put(current.right)

    return sum

print(find_sum_bfs(a)) # 21