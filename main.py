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

print("")

ll = LinkedList(1)
ll.append(1)
ll.append(1)
ll.append(1)

print(ll.binary_to_decimal())


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Partition in Middle
    print("Test 1: Partition in Middle")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 2, 4, 5, 8, 10]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: Partition at Start
    print("Test 2: Partition at Start")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [2, 5, 8, 3, 10, 4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Partition at End
    print("Test 3: Partition at End")
    x = 11
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 8, 3, 10, 2, 4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Empty List
    print("Test 4: Empty List")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.make_empty()
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if ll.head is None:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: All Greater or Equal
    print("Test 5: All Greater or Equal")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [6, 7, 8]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 6, 7, 8]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: Single Element
    print("Test 6: Single Element")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(4)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Duplicates Equal to x
    print("Test 7: Duplicates Equal to x")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    for i in [1, 3, 2, 3]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 8: Already Partitioned
    print("Test 8: Already Partitioned")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    for i in [2, 5, 8, 10]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 5, 8, 10]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 8 tests passed.")


# Run the test function
test_partition_list()

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("BEFORE: ", end="")
ll1.print_list()
print("AFTER:  ", end="")
ll1.swap_pairs()
ll1.print_list()
print("-----------------------------------")

# Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
print("BEFORE: ", end="")
ll2.print_list()
print("AFTER:  ", end="")
ll2.swap_pairs()
ll2.print_list()
print("-----------------------------------")

# Test case 3: Swapping pairs in a list with a single node (1)
print("\nTest case 3: Swapping pairs in a list with a single node.")
ll3 = LinkedList(1)
print("BEFORE: ", end="")
ll3.print_list()
print("AFTER:  ", end="")
ll3.swap_pairs()
ll3.print_list()
print("-----------------------------------")

# Test case 4: Swapping pairs in an empty list
print("\nTest case 4: Swapping pairs in an empty list.")
ll4 = LinkedList(1)
ll4.make_empty()
print("BEFORE: ", end="")
ll4.print_list()
print("AFTER:  ", end="")
ll4.swap_pairs()
ll4.print_list()
print("-----------------------------------")

# Test case 5: Swapping pairs in a list with two nodes (1->2)
print("\nTest case 5: Swapping pairs in a list with two nodes.")
ll5 = LinkedList(1)
ll5.append(2)
print("BEFORE: ", end="")
ll5.print_list()
print("AFTER:  ", end="")
ll5.swap_pairs()
ll5.print_list()
print("-----------------------------------")


