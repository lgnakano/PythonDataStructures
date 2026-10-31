from DoublyLinkedListNode import DoublyLinkedListNode


class DoublyLinkedList:
    def __init__(self, value):
        new_node = DoublyLinkedListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        return_value = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return_value.prev = None
        self.length -= 1
        return return_value

