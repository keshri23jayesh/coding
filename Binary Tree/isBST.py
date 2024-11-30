
class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class isBstDs:
    def __init__(self, max, min, isbst):
        self.max = max
        self.min = min
        self.isbst = isbst


class BST:

    def __init__(self):
        self.root = None

    def _insert(self, root, key):
        if key > root.value:
            if not root.right:
                root.right = Node(key)
                return
            self._insert(root.right, key)
        else:
            if not root.left:
                root.left = Node(key)
                return
            self._insert(root.left, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        self._insert(self.root, key)

    def level_order(self):
        level = [self.root]
        while level:
            level_len = len(level)
            current_level = " "
            for i in range(0, level_len):
                node = level.pop(0)
                current_level += str(node.value) + " "
                if node.left:
                    level.append(node.value)
                if node.right:
                    level.append(node.value)
            print(current_level)

    def isBST(self, node):
        if not node:
            return isBstDs(-100000, 100000,True)

        is_left_bst = self.isBST(node.left)
        is_right_bst = self.isBST(node.right)

        is_bst_node = (is_right_bst.isbst and
                       is_left_bst.isbst and
                       is_left_bst.max <= node.value <= is_right_bst.min)

        max_val = max(node.value, max(is_left_bst.max, is_right_bst.max))
        min_val = min(node.value, min(is_left_bst.min, is_right_bst.min))

        return isBstDs(max_val, min_val, is_bst_node)


bst = BST()
elements = [50, 25, 12, 37, 75, 62, 87]
# elements = [50, 25, 75]

for elem in elements:
    bst.insert(elem)

val = bst.isBST(bst.root)
print(val.min)
print(val.max)
print(val.isbst)