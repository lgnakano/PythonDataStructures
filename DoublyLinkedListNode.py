class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def print(self):
        print("Node:")
        print(self)
        print("value:")
        print(self.value)
        print("next:")
        print(self.next)
        print("prev:")
        print(self.prev)