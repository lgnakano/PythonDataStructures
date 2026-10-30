class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        print("Node:")
        print("value:")
        print(self.value)
        print("next:")
        print(self.next)