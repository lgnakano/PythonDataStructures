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

def reverse_string(string):
    my_stack = Stack_List()
    for charpos in range(len(string)):
        my_stack.push(string[charpos])
    ret_string = ""
    while my_stack.is_empty() is not True:
        ret_string += my_stack.pop()
    return ret_string




my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""

# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
#                                             #
#    This is a separate function that is      #
#    not a method within the Stack class.     #
#    Indent all the way to the left.          #
#                                             #
###############################################
def is_balanced_parentheses(string):
    my_stack = Stack_List()
    for charpos in range(len(string)):
        if string[charpos] == "(":
            my_stack.push(string[charpos])
        else:
            if string[charpos] == ")":
                top = my_stack.pop()
                if top != "(":
                    return False
    return my_stack.is_empty()

def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()


##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################

def sort_stack(input_stack):
    sorted_stack = Stack_List()
    while input_stack.is_empty() is False:
        temp = input_stack.pop()
        while sorted_stack.is_empty() is False and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while sorted_stack.is_empty() is False:
        input_stack.push(sorted_stack.pop())
    return sorted_stack


my_stack = Stack_List()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""