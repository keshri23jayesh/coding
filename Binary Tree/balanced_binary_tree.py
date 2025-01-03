# https://www.youtube.com/watch?v=9X1TYiipolA&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=50
class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class isBBstDs:
    def __init__(self, height, is_balanced):
        self.height = height
        self.is_balanced = is_balanced


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

    def is_balanced_binary_tree(self, node):
        """
        balanced definition is |l_height - r_height| <= 1
        :param node:
        :return:
        """

        if not node:
            return isBBstDs(0, True)

        left_balanced = self.is_balanced_binary_tree(node.left)
        right_balanced = self.is_balanced_binary_tree(node.right)

        balanced = False
        if (left_balanced.is_balanced and right_balanced.is_balanced
                and abs(left_balanced.height - right_balanced.height) <= 1):
            balanced = True
        height = max(left_balanced.height, right_balanced.height) + 1
        return isBBstDs(height, balanced)



# bst = BST()
# elements = [50, 25, 12, 37, 75, 62, 87]
# # elements = [50, 25, 75]
#
# for elem in elements:
#     bst.insert(elem)
#
# is_it_bbst = bst.is_balanced_binary_tree(bst.root)
# print(is_it_bbst)



bst = BST()
elements = [50, 25, 12, 5, 3,  75, 87]
# elements = [50, 25, 75]

for elem in elements:
    bst.insert(elem)

is_it_bbst = bst.is_balanced_binary_tree(bst.root)
print(is_it_bbst)