from Stack_List import Stack_List

my_stack = Stack_List()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1

"""

my_stack = Stack_List()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1

    Popped node:
    3

    Stack after pop():
    2
    1

"""