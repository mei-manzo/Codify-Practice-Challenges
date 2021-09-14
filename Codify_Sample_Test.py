
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
    for x in A:
        if x>maximum:
            maximum=x
        else:
            pass
        return maximum
    for x in A:
        if x < -1000000 or x > 10000000:
            return "Out of bounds"
        elif x > 100000:
            return "Out of bounds"
        else:
            pass
    

print(solution([1,2,3]))
print("done")

# def ult_analysis(A): 
#     maximum = 0
#     for x in A:
#         if x>maximum:
#             maximum = x
#     return{ 'maximum': maximum}
# print(ult_analysis([100,200,10,-9]))