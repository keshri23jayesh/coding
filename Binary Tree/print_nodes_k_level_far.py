# https://www.youtube.com/watch?v=cH8gtWOrTGY&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=25

"""
the solution approach takes two things,
1. node to root path
2. and print k levels down.
(take care of one point, not to print duplicate caused by
print k levels down, we have to pass a blocker not to go that side.)
"""


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

    def node_to_root_path(self, elem, node):
        if not node:
            return False
        if node.value == elem:
            self.path.append(node)
            self.found = True
            return

        if not self.found:
            self.node_to_root_path(elem, node.left)
        if not self.found:
            self.node_to_root_path(elem, node.right)
        if self.found:
            self.path.append(node)

    def print_k_level_down(self, level, node, blocker):

        if not node or level < 0:
            return

        if blocker and node.value == blocker.value:
            return

        if level == 0:
            print(node.value)
            return

        self.print_k_level_down(level-1, node.left, blocker)
        self.print_k_level_down(level-1, node.right, blocker)

    def print_k_levels_far(self, value, level_far):
        self.node_to_root_path(value, self.root)
        for i in range(0, len(self.path)):
            blocker = self.path[i-1] if i > 0 else None
            self.print_k_level_down(level_far-i, self.path[i], blocker)


# random_values = random.sample(range(1, 101), 20)

nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

# bst.level_order()
bst.print_k_levels_far(value=75, level_far=3)







