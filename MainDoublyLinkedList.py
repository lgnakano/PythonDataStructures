from DoublyLinkedList import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# my_doubly_linked_list.print_list()

# (2) Items - Return 2 Node
print(my_doubly_linked_list.pop())
# (1) Item - Return 1 Node
print(my_doubly_linked_list.pop())
# (0) Item - Return None
print(my_doubly_linked_list.pop())