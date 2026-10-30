from node import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length != 0:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != None and fast != self.tail:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        return slow

    def has_loop(self):
        slow = self.head.next
        fast = self.head.next
        fast = fast.next
        while fast != None and fast != self.tail:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        if fast == None or fast == self.tail:
            return False

    def remove_duplicates(self):
        current = self.head
        while current is not None:
            runner = current
            while runner is not None:
                if runner.next is None:
                    break
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
        return True

    def binary_to_decimal(self):
        decimal = 0
        current = self.head
        while current is not None:
            decimal = 2 * decimal + current.value
            current = current.next
        return decimal

    def partition_list(self, x):
        if self.head is None:
            return None
        dummy_1 = Node(0)
        dummy_2 = Node(0)

        print(dummy_1.next)
        print(dummy_2.next)

        prev1 = dummy_1
        prev2 = dummy_2

        current = self.head
        while current is not None:
            print("value:")
            print(current.value)
            print("next:")
            print(current.next)
            if current.value < x:
                print("dummy_1.next")
                print(dummy_1.next)
                print("prev1")
                prev1.next = current
                prev1 = current
                prev1.print()
            else:
                print("dummy_2.next")
                print(dummy_2.next)
                print("prev2")
                prev2.next = current
                prev2 = current
                prev2.print()
            current = current.next

        prev2.next = None
        prev1.next = dummy_2.next
        self.head = dummy_1.next
