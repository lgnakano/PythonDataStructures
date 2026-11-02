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

print("Testing Prepend")

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()
print("Testing pop_first")
print(my_doubly_linked_list.pop_first().value)

print("printing remaining list")
my_doubly_linked_list.print_list()

print("Testing pop_first")
print(my_doubly_linked_list.pop_first().value)

print("printing remaining list")
my_doubly_linked_list.print_list()

print("Testing pop_first")
print(my_doubly_linked_list.pop_first().value)

print("printing remaining list")
my_doubly_linked_list.print_list()

print("Testing pop_first")
print(my_doubly_linked_list.pop_first())

print("printing remaining list")
my_doubly_linked_list.print_list()

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print("testing get(0)")
print(my_doubly_linked_list.get(0).value)

print("testing get(1)")
print(my_doubly_linked_list.get(1).value)

print("testing get(2)")
print(my_doubly_linked_list.get(2).value)

print("testing get(3)")
print(my_doubly_linked_list.get(3).value)

print("testing get(4)")
print(my_doubly_linked_list.get(4))

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print("Original list")
my_doubly_linked_list.print_list()
my_doubly_linked_list.set_value(1, 4)
print("Updated list")
my_doubly_linked_list.print_list()

print("Original list")
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(1, 2)
print("After inserting at index 1")
my_doubly_linked_list.print_list()

print("Testing Remove")

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()
