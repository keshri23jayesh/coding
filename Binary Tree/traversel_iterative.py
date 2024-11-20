
class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def _insert(self, root, key):
        if key < root.value:
            if not root.left:
                root.left = Node(key)
                return
            self._insert(root.left, key)
        else:
            if not root.right:
                root.right = Node(key)
                return
            self._insert(root.right, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def iterative_print(self):
        stack = list()
        PRE = ''
        IN = ''
        POST = ''
        stack.append((self.root, 1))
        while len(stack):
            top = stack.pop()
            node = top[0]
            if top[1] == 1:
                PRE += " " + str(node.value)
                stack.append((top[0], 2))
                if node.left:
                    node = node.left
                    stack.append((node, 1))
            elif top[1] == 2:
                IN += " " + str(node.value)
                stack.append((top[0], 3))
                if node.right:
                    node = node.right
                    stack.append((node, 1))
            else:
                POST += " " + str(top[0].value)
        print("IN -", IN)
        print("POST -", POST)
        print("PRE -", PRE)


bst = BST()

elements = [50, 25, 12, 37, 75, 62, 87]

for elem in elements:
    bst.insert(elem)
print(bst.root)
bst.iterative_print()
