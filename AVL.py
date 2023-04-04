import time

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def build_avl_tree(self, keys):
        keys = sorted(keys)

        def _build_avl_tree(start, end):
            if len(keys) == 0:
                return None

            if start > end:
                return None

            mid = (start + end) // 2
            node = AVLNode(keys[mid])

            node.left = _build_avl_tree(start, mid - 1)
            node.right = _build_avl_tree(mid + 1, end)

            node.height = 1 + max(self.height(node.left), self.height(node.right))

            return node

        self.root = _build_avl_tree(0, len(keys) - 1)

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        left_child = node.left
        right_child_of_left_child = left_child.right

        left_child.right = node
        node.left = right_child_of_left_child

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + max(self.height(left_child.left), self.height(left_child.right))

        return left_child

    def rotate_left(self, node):
        right_child = node.right
        left_child_of_right_child = right_child.left

        right_child.left = node
        node.right = left_child_of_right_child

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + max(self.height(right_child.left), self.height(right_child.right))

        return right_child

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return AVLNode(key)

            if key < node.key:
                node.left = _insert(node.left, key)

            else:
                node.right = _insert(node.right, key)

            node.height = 1 + max(self.height(node.left), self.height(node.right))

            balance = self.get_balance(node)

            if balance > 1 and key < node.left.key:
                return self.rotate_right(node)

            if balance < -1 and key > node.right.key:
                return self.rotate_left(node)

            if balance > 1 and key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            if balance < -1 and key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = _insert(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if node is None:
                return node

            if key < node.key:
                node.left = _delete(node.left, key)

            elif key > node.key:
                node.right = _delete(node.right, key)

            else:
                if node.left is None and node.right is None:
                    node = None

                elif node.left is None:
                    node = node.right

                elif node.right is None:
                    node = node.left

                else:
                    temp = self.find_min(node.right)

                    node.key = temp.key

                    node.right = _delete(node.right, temp.key)

            if node is None:
                return node

            node.height = 1 + max(self.height(node.left), self.height(node.right))

            balance = self.get_balance(node)

            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.rotate_right(node)

            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.rotate_left(node)

            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = _delete(self.root, key)

    def find_min(self, node):
        current = node
        print(current.key)
        while current.left is not None:
            current = current.left
            print(current.key)
        return current

    def find_max(self, node):
        current = node
        print(current.key)
        while current.right is not None:
            current = current.right
            print(current.key)
        return current

    def display_inorder(self, node):
        if node is not None:
            self.display_inorder(node.left)
            print(node.key, end=' ')
            self.display_inorder(node.right)

    def display_preorder(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.display_preorder(node.left)
            self.display_preorder(node.right)

    def display_subtree_preorder(self, key):
        def _display(node, key):
            if node is not None:
                if node.key == key:
                    print(node.key, end=' ')
                    self.display_preorder(node.left)
                    self.display_preorder(node.right)
                else:
                    _display(node.left, key)
                    _display(node.right, key)

        _display(self.root, key)

    def delete_postorder(self, node):
        if node is not None:
            self.delete_postorder(node.left)
            self.delete_postorder(node.right)
            print(node.key, end=' ')
            del node

    def display(self):
        def _display(node, level=0):
            if node is not None:
                _display(node.right, level + 1)
                print('   ' * level + '->', node.key, '[', node.height, ']')
                _display(node.left, level + 1)

        _display(self.root)

avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(25)
avl_tree.insert(35)
avl_tree.insert(45)
avl_tree.insert(55)
avl_tree.insert(60)
avl_tree.insert(70)
avl_tree.insert(80)
avl_tree.display()

avl_tree.delete(30)
avl_tree.display()

avl_tree.find_max(avl_tree.root)
avl_tree.find_min(avl_tree.root)

avl_tree.display_inorder(avl_tree.root)
print()
avl_tree.display_preorder(avl_tree.root)
print()
avl_tree.display_subtree_preorder(35)
print()
avl_tree.delete_postorder(avl_tree.root)
print()

avl_tree2 = AVLTree()
avl_tree2.build_avl_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
avl_tree2.display()
print()
avl_tree2.delete(6)
avl_tree2.display()
print()
