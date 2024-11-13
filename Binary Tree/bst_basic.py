class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:

    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def _search(self, node, key):
        if node is None or key == node.value:
            return node
        elif key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

    def search(self, key):
        self._search(self.root, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def display(self):
        values = self.inorder()
        print("BST In-order Traversal:", values)


    def display_in_problem_1(self):
        node = self.root

        def _display_in_problem_1(node):
            if not node:
                return
            string_left = " . " if not node.left else str(node.left.value)
            string_right = " . " if not node.right else str(node.right.value)
            string = string_left + "<-" + str(node.value) + "->" + string_right
            print(string)
            _display_in_problem_1(node.left)
            _display_in_problem_1(node.right)

        _display_in_problem_1(node)


bst = BST()

# elements = [20, 10, 30, 5, 15, 25, 35]
elements = [50, 25, 12, 37, 30, 75, 62, 70, 87]
for elem in elements:
    bst.insert(elem)

# bst.display()


# https://www.youtube.com/watch?v=sYU6AnSJyjo&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=3
# print in given order
bst.display_in_problem_1()



