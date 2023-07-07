from fib import FibHeap

# Please read all of the following before starting your implementation:
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit the requirements.py and the fib.py files, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - We have provided a project2_tests.py file that contains some simple test cases to give an idea of how we will be running your
#   code. Please use that file when testing your implementation.
#
#
# We have provided a node class called FibNode which you will use to create the nodes within the Fibonacci heap.
# Please do not make a different node class, as this will interfer with checking the correctness of the code
#
# Explanations for FibHeap public member functions
# 
# Note: you may assume that each function will be called with valid values during testing
# init(): initializes the Fibonacci heap as an empty heap with no nodes. We have predefined a few variables for you. Feel free to use them or define your own.
# 				
# get_roots(): will be used to check the correctness of the heap structure. It returns a list of all the root nodes in the heap.
#
# Methods that need to be completed:
#
# insert(value): insert an item with the specified value to the Fibonacci heap. you want to return the node that you created.
#                you can assume that the value is not already in the heap.
#
# delete_min(): deletes the minimum node from the Fibonacci heap. you can assume that the heap is non-empty when this is called.
#
# find_min(): returns the node with the minimum value in the Fibonacci heap. you can assume that the heap is non-empty when this is called.
#
# decrease_priority(node, new_val): decreases the priority of the specified node to the new value. you can assume that the new value is 
#                                   less than the current value and that it will not decrease to a pre-existing priority in the heap.
