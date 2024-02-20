#######################################################################
# Mission 1: Write a program which fulfills the requirements below
# Description
# We want you to calculate the sum of squares of given integers, excluding any negatives.
# The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
# Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.
# Note: There should be no output until all the input has been received.
# Note 2: Do not put blank lines between test cases solutions.
# Note 3: Take input from standard input, and output to standard output.
# Rules
# Write your solution using Go Programming Language or Python Programming Language. Do not submit your solution with both languages at once!

# You may only use standard library packages. In addition, extra point is awarded if solution does not declare any global variables.

# Specific rules for Python solution
# Your source code must be a single file, containing at least a main function
# Do not use any for loop, while loop, or any list / set / dictionary comprehension
# Your solution will be tested against Python 3.11 (as of February 2023) or higher
# def main():
#     ...

# if __name__ == "__main__":
#     main()

# Sample Input
# 2
# 4
# 3 -1 1 14
# 5
# 9 6 -53 32 16

# Sample Output
# 206
# 1397
#######################################################################

import sys

# NOT A GLOBAL VARIABLE, ONLY FUNCTION
# map function
square_map = lambda x : x*x
sum_map = lambda x: x

# filter function
pos_filter = lambda x: x>0

def get_iteration_times():
    """get the iteration times of input cases: N
    N is in the range: 1 <= N <= 100 """
    try:
        n = int(input())
        if n <= 0 or n > 100:
            sys.stderr.write("iteration times N (1 <= N <= 100)\n")
            sys.exit(1);
    except ValueError:
        sys.stderr.write("First input should be a integer N, that 1<= N <=100\n")
        sys.exit(1)
    return n

def get_data():
    """parse standard input, first get a integer X(0 < X <= 100)
    then followed by X integers Yn(-100 <= Yn <= 100) space-separated on next line"""
    try:
        X = int(input())
        if X <= 0 or X > 100:
            sys.stdin.readline() # dump the rest data
            raise ValueError
        Y = map(int, sys.stdin.readline().split())
    except ValueError:
        sys.stderr.write("Input Data Error: ")
        raise ValueError
    return Y

def calculate(times, map_func = sum_map, filter_fun = pos_filter):
    """get data, and calculate a """
    if times == 0:
        return 0
    try:
        result = sum(map(map_func, filter(filter_fun, get_data())))
        print(result)
    except ValueError:
        sys.stderr.write("at %d input dataset\n" % (times))
    return calculate(times-1, map_func, filter_fun)

def main():
  n = get_iteration_times()
  calculate(n, square_map, pos_filter)

if __name__ == "__main__":
  main()
