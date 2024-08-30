# node_binary_tree.py

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def inorder_traversal(self, node, values):
        if node is not None:
            self.inorder_traversal(node.left, values)
            values.append(node.value)
            self.inorder_traversal(node.right, values)

    def inorder(self):
        values = []
        self.inorder_traversal(self.root, values)
        return values

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None or current_node.value == key:
            return current_node

        if key < current_node.value:
            return self._search(current_node.left, key)

        return self._search(current_node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example Usage
if __name__ == "__main__":
    tree = Binary_Tree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("Inorder traversal of the given tree")
    print(tree.inorder())

    print("\nDelete 20")
    tree.delete(20)
    print("Inorder traversal after deleting 20")
    print(tree.inorder())

    print("\nDelete 30")
    tree.delete(30)
    print("Inorder traversal after deleting 30")
    print(tree.inorder())

    print("\nDelete 50")
    tree.delete(50)
    print("Inorder traversal after deleting 50")
    print(tree.inorder())