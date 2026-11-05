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


print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

print("Testing reverse_between")

# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs()


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""