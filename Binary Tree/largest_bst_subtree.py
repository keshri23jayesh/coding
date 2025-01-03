
class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class isBBstDs:

    def __init__(self, size, is_balanced, node, min_value, max_value):
        self.size = size
        self.is_balanced = is_balanced
        self.largest_bst_root = node
        self.min_value = min_value
        self.max_value = max_value


class BST:

    def __init__(self):
        self.root = None
        self.bst_max_height = 0

    def _insert(self, node, key):
        if node.value > key:
            if not node.left:
                node.left = Node(key)
                return
            self._insert(node.left, key)
        else:
            if not node.right:
                node.right = Node(key)
                return
            self._insert(node.left, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def level_order(self):
        levels = [self.root]
        while len(levels):
            level_len = len(levels)
            current_level = " "
            for i in range(0, level_len):
                elem = levels.pop(0)
                current_level += str(elem.value) + " "
                levels.append(elem.left) if elem.left else None
                levels.append(elem.right) if elem.right else None
            print(current_level)

    def largest_bst(self, node):
        if not node:
            return isBBstDs(0, True, None, -100000, 100000)
        left_bbst = self.largest_bst(node.left)
        right_bbst = self.largest_bst(node.right)

        is_balanced = False
        if (left_bbst.is_balanced and right_bbst.is_balanced
                and right_bbst.min_value > node.data > left_bbst.max_value):
            is_balanced = True

        min_value = min(node.data, min(left_bbst.min_value, right_bbst.min_value))
        max_value = max(node.data, max(left_bbst.max_value, right_bbst.max_value))

        if is_balanced:
            size = max(left_bbst.size, right_bbst.size) + 1
            root = node
        elif left_bbst.size > right_bbst.size:
            root = left_bbst.largest_bst_root
            size = left_bbst.size
        else:
            root = right_bbst.largest_bst_root
            size = right_bbst.size
        return isBBstDs(size, is_balanced, root, min_value, max_value)


bst = BST()
elements = [50, 25, 12, 5, 3,  75, 87]
# elements = [50, 25, 75]

for elem in elements:
    bst.insert(elem)

bst.largest_bst(bst.root)
print(bst.bst_max_height)
