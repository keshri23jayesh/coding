# https://www.youtube.com/watch?v=S0Bwgtn32uI&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=45

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

    def diameter_optimised(self, node):
        if not node:
            return 0

        l_height = self.height(node.left)
        r_height = self.height(node.right)

        diameter = l_height + r_height

        l_diameter = self.diameter_optimised(node.left)
        r_diameter = self.diameter_optimised(node.right)

        return max(l_diameter, r_diameter, diameter)
        pass
    

nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

# bst.level_order()
bst.print_k_levels_far(value=75, level_far=3)





