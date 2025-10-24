#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)


def print_numbers(numbers):
    for i in range(len(numbers)):
        print(numbers[i])


def Fibonacci_calculator(n):
    fibonacci_numbers = []
    if n == 0:
        return fibonacci_numbers
    fibonacci_numbers.append(0)
    if n == 1:
        return fibonacci_numbers
    previous_num = 0
    current_num = 1
    next_num = 0
    for i in range(1,n):
        next_num = previous_num+current_num
        previous_num = current_num
        current_num = next_num
        fibonacci_numbers.append(current_num)
    return fibonacci_numbers


def user_input():
    n = int(input("Enter a positive integer: "))
    
    while n <= 0:
        n = int(input("Invalid input. Please enter a positive integer: "))
    
    return n