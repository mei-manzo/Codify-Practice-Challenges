
# Task 1

# Python
# Task description
# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):#takes an array A
    maximum = 0
    num_negatives = []
    num_positives = []
    #works for integer array with gaps
    for x in A:
        if x < 0: #creating an array of negative values
            num_negatives.append(x)
        if len(num_negatives) == len(A): #if all ints in array are negative, n=1
            n = 1
        elif x > 0: #creating new array of positive integers
            num_positives.append(x)
        if len(num_positives) == 1 and num_positives[0] != 1: #if just one positive integer higher than 1, n will be int minus 1
            return (num_positives[0]-1)
        if len(num_positives) == 1 and num_positives[0] == 1:#if single positive integer is 1, n will be 2
            return 2
        elif len(num_positives) > 1: #now need to implement more checks to see if there are gaps
            return ("other case")
print(solution([-3,-4,-10,20]))
print("finished")
