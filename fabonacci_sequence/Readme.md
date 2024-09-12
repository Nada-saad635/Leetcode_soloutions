# Fibonacci Sequence Generator

This Python script generates the Fibonacci sequence up to the nth number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1.

## How the Fibonacci Sequence Works

The Fibonacci sequence starts with two numbers: 0 and 1. Each subsequent number is the sum of the previous two numbers. For example:


In this example:
- 0 + 1 = 1
- 1 + 1 = 2
- 1 + 2 = 3
- 2 + 3 = 5
- 3 + 5 = 8

## How to Use the Code

## Customizing the Output
You can modify the variable `n` to generate more or fewer Fibonacci numbers. For example, to generate the first 15 numbers, change `n` to 15:



n = 11
sequence = fibonacci_sequence(n)
print(sequence)

This will output:s
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

