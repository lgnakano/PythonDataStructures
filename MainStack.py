from Stack import Stack

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop().value, "\n")

my_stack.print_stack()
