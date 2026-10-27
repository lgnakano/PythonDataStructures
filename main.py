from linkedList import LinkedList

my_linked_list = LinkedList(1)

# my_node = my_linked_list.pop()

# print(my_node.value)

# my_linked_list.append(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item - Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()

my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Items - Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2).value)

print("")

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1, 4)
my_linked_list.print_list()

print("")

my_linked_list = LinkedList(0)
my_linked_list.append(2)
my_linked_list.insert(1,1)

my_linked_list.print_list()

print("")

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')

my_linked_list.print_list()

print("")

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()

print("")

my_linked_list.reverse()

my_linked_list.print_list()

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast == None:
            return None
        fast = fast.next
    while fast != None:
        slow = slow.next
        fast = fast.next
    return slow

#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])