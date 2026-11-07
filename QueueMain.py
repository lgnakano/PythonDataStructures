from Queue import Queue

my_queue = Queue(1)

my_queue.enqueue(2)

my_queue.print_queue()

my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""

print("Testing dequeue: original queue")

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()

print("Testing dequeue: value returned by dequeue()")
# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)

print("Testing dequeue: value returned by dequeue()")
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)

print("Testing dequeue: value returned by dequeue()")
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""