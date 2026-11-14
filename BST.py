from BSTNode import BSTNode

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return True
        else:
            current = self.root
            while True:
                if data == current.value:
                    return False
                if data < current.value:
                    if current.left is None:
                        current.left = BSTNode(data)
                        return True
                    current = current.left
                else:
                    if current.right is None:
                        current.right = BSTNode(data)
                        return True
                    current = current.right

    def contains(self, data):
        current = self.root
        while current is not None:
            if data < current.value:
                current = current.left
            elif data > current.value:
                current = current.right
            else:
                return True
        return False