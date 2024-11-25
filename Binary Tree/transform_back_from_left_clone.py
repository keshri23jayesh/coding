# https://www.youtube.com/watch?v=YCd-jyAF0CM&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=37

class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.path = []
        self.found = False

    def _insert(self, root, key):
        if key <= root.value:
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

    def level_order(self, node):
        if not node:
            return
        level = [node]
        while len(level):
            count = len(level)
            current_level = ""
            for i in range(0, count):
                elem = level.pop(0)
                current_level += str(elem.value) + " "
                if elem.left:
                    level.append(elem.left)
                if elem.right:
                    level.append(elem.right)
            print(current_level)

    def transform_back(self, node):
        if not node:
            return
        if node and node.left and node.value == node.left.value:
            node.left = node.left.left
        self.transform_back(node.left)
        self.transform_back(node.right)


"""
expected

50 
50 75 
25 75 87 
25 37 62 87 90 
12 37 62 90 
12 

"""

nodes = [50, 50, 75, 25, 75, 87, 25, 37, 62, 87, 90, 12, 37, 62, 90, 12]

bst = BST()
for node in nodes:
    bst.insert(node)
bst.level_order(bst.root)
bst.transform_back(bst.root)
print("-----------")
bst.level_order(bst.root)
