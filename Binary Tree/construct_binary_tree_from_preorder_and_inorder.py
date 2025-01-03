# https://www.youtube.com/watch?v=oAbSNJ35qAs&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=55

"""
whenever visit this next time, pls check once.
faced problem while calculating post order range and handling base case.
"""

class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


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

    def convert_to_tree(self, preorder, inorder, pre_si, pre_ei, isi, iei):
        # Base case: if there's no subtree
        if pre_si > pre_ei or isi > iei:
            return None

        # Root value is the last element in the current postorder range
        root_value = preorder[pre_ei]
        root_node = Node(root_value)

        # Find the root index in the inorder list
        root_idx = inorder.index(root_value)

        # Calculate the size of left and right subtrees
        left_tree_size = root_idx - isi
        right_tree_size = iei - root_idx

        # Recursively construct the left subtree
        root_node.left = self.convert_to_tree(preorder, inorder,
                                              pre_si+1, pre_si + left_tree_size,
                                              isi, root_idx - 1)

        # Recursively construct the right subtree
        root_node.right = self.convert_to_tree(preorder, inorder,
                                               pre_si + left_tree_size + 1, pre_ei,
                                               root_idx + 1, iei)
        return root_node
