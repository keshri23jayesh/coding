# https://www.youtube.com/watch?v=TO7trQloRXc&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=33

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

    def left_cloned_tree(self, node):
        if not node:
            return

        left = self.left_cloned_tree(node.left)
        right = self.left_cloned_tree(node.right)

        new_node = Node(node.value)
        new_node.left = Node(node.value)
        new_node.left.left = left
        new_node.right = right

        return new_node
        #
        # if from_left and parent:
        #     new_node = Node(node.value)
        #     new_node.left = parent.left
        #     parent.left = new_node




# nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]
nodes = [50, 25, 12, 37, 75, 62, 87, 90]
# nodes = ['a', ]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

bst.level_order(bst.root)
new_node = bst.left_cloned_tree(bst.root)
# print(new_node)
print("-------")
bst.level_order(new_node)
