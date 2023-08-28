#!/usr/bin/env python3
def print_fibonacci(length): # The function is defined with a single parameter 'length' which represents the desired length of the Fibonacci sequence.
    fib_seq = [] # An empty list to store the Fibonacci sequence.
    if length > 0:
        fib_seq.append(0) #If the desired length is greater than 0, the first element '0' is appened to fib_seq list.
    if length >= 2:
        fib_seq.append(1) # If desired length is greater than or equal to 2, the 2nd element '1' is appended to the fib_seq list. This is because the Fibonacci sequence typically srarts with [0,1].
        for i in range(2, length):
            fib_seq.append(fib_seq[-1] + fib_seq[-2]) #Starting from index 2, a loop iterates from2 to 'length -1'. In each iteration, the next Fibonacci number is computed as the sum of the last two elements in the fib_seq list and is appended to the list.
    print(fib_seq)