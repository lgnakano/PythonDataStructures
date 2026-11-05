from QueueNode import QueueNode

class Queue:
    def __init__(self, value):
        new_node = QueueNode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
