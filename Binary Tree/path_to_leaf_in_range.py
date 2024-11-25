# https://www.youtube.com/watch?v=A6Z5YvsrDtg&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=29

# we have to print path both inclusive and exclusive.

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

    def print_node_to_root(self, node, range, arr):
        if not node:
            if range[0] < sum(arr) < range[1]:
                print(arr, sum(arr))
            return
        """
        if node.left and node.right is not there, 
        we can add node last level, and print the result.
        reason last nore is not added
        """

        # if not node:
        #     return
        #
        # if node and not node.left and not node.right:
        #     if range[0] < sum(arr) < range[1]:
        #         print(arr, sum(arr))
        #     return
        #
        # if len(arr) > 6:
        #     print('here')

        arr.append(node.value)
        self.print_node_to_root(node.left, range, arr)
        self.print_node_to_root(node.right, range, arr)
        arr.pop()

# [28, 29, 61, 43, 52, 59, 55, 58] 385
# [28, 29, 61, 75, 90, 96] 379

"""
                                 28
                         7              29
                22                              61
        16                          43                    75
                                           52       63             90
                                        46    59        64      78                                                             96
                                            55              74      84 
                                               58
"""


nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

# bst.level_order()
bst.print_node_to_root(bst.root, [378, 386], [])






