# https://www.youtube.com/watch?v=Lc3RBGtyn7M&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=54

# notes -
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

    def convert_to_tree(self, postorder, inorder, psi, pei, isi, iei):
        # Base case: if there's no subtree
        if psi > pei or isi > iei:
            return None

        # Root value is the last element in the current postorder range
        root_value = postorder[pei]
        root_node = Node(root_value)

        # Find the root index in the inorder list
        root_idx = inorder.index(root_value)

        # Calculate the size of left and right subtrees
        left_tree_size = root_idx - isi
        right_tree_size = iei - root_idx

        # Recursively construct the left subtree
        root_node.left = self.convert_to_tree(
            postorder, inorder,
            psi, psi + left_tree_size - 1,  # Postorder range for the left subtree
            isi, root_idx - 1  # Inorder range for the left subtree
        )

        # Recursively construct the right subtree
        root_node.right = self.convert_to_tree(
            postorder, inorder,
            psi + left_tree_size, pei - 1,  # Postorder range for the right subtree
            root_idx + 1, iei  # Inorder range for the right subtree
        )

        return root_node


postorder = [7, 8, 3, 9, 10, 4, 1, 11, 5, 6, 2, 0]
inorder  =  [7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 2, 6]

psi = 0
pei = len(postorder) - 1


isi = 0
iei = len(inorder) - 1


node = BST().convert_to_tree(postorder, inorder, psi, pei, isi, iei)
print(node)
