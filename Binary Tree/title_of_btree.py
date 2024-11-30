# https://www.youtube.com/watch?v=CVXfXjuBM8I&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=46

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

    def level_order(self):
        levels = [self.root]
        while len(levels):
            count = len(levels)
            elem = ""
            for i in range(0, count):
                node = levels.pop(0)
                elem += " " + str(node.value)
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            print(elem)

    def height(self, node):
        if not node:
            return 0
        left_height = 1 + self.height(node.left)
        right_height = 1 + self.height(node.right)
        return max(left_height, right_height)

    def tilt(self, node):
        if not node:
            return 0, None

        left_sum, left_node = self.tilt(node.left)
        right_sum, right_node = self.tilt(node.right)

        abs_diff = abs(left_sum-right_sum)
        new_node = Node(abs_diff)

        new_node.left = left_node
        new_node.right = right_node

        return left_sum + right_sum + node.value, new_node


bst = BST()
elements = [50, 25, 12, 37, 75, 62, 87]
# elements = [50, 25, 75]

for elem in elements:
    bst.insert(elem)

data = bst.tilt(bst.root)
print(data)










