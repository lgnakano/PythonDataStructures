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

    def prepend(self, value):
        new_node = DoublyLinkedListNode(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.length += 1
        self.head = new_node
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        if index < 0 or index > self.length:
            return False
        after = self.get(index)
        before = after.prev
        new_node = DoublyLinkedListNode(value)
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def is_palindrome(self):
        if self.length <= 1:
            return True
        before = self.head
        after = self.tail
        for _ in range(self.length//2):
            if before.value != after.value:
                return False
            before = before.next
            after = after.prev
        return before.value == after.value

    def reverse(self):
        if self.length == 0:
            return
        current = self.head
        while current is not None:
            temp_next = current.next
            current.next = current.prev
            current.prev = temp_next
            current = temp_next
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        if self.head is None:
            return None
        dummy_1 = DoublyLinkedListNode(0)
        dummy_2 = DoublyLinkedListNode(0)

        prev1 = dummy_1
        prev2 = dummy_2

        current = self.head
        while current is not None:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next

        prev2.next = None
        if dummy_2.next is None:
            self.tail = prev1
        else:
            prev1.next = dummy_2.next
            dummy_2.next.prev = prev1
        print("before assigning head")
        print(dummy_1.next.value)
        self.head = dummy_1.next
        self.tail.next = None
