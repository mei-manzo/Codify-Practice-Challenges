
# Task 1

# Python
# Task description
# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5. *PASS*

# Given A = [1, 2, 3], the function should return 4. *PASS*

# Given A = [−1, −3], the function should return 1. *PASS*

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):#takes an array A
    maximum = 0
    num_negatives = []
    num_positives = []
    for x in A:
        if x < 0: #creating an array of negative values
            num_negatives.append(x)
        if len(num_negatives) == len(A): #if all ints in array are negative, n=1
            n = 1
            return n
    for x in A:
        if x > 0: #creating new array of positive integers
            num_positives.append(x)
    for x in A:#tested, is accessing positives
        if len(num_positives) == 1 and num_positives[0] != 1: #if just one positive integer higher than 1, n will be int minus 1
            print(num_positives) #printing only one value? debug this
            return (num_positives[0]-1)
        elif len(num_positives) == 1 and num_positives[0] == 1:#if single positive integer is 1, n will be 2
            return 2
        elif len(num_positives) > 1: #now need to implement more checks to see if there are gaps
            # find lowest, find highest. create a dictionary incrementing in steps of 1 using those values
            minimum = num_positives[0]
            maximum = num_positives[0]
            gap_nums = []
            for u in num_positives:
                if u < minimum:
                    minimum = u #sets the minimum
                else:
                    pass
            for i in num_positives:
                if i > maximum:
                    maximum = i
                else:
                    pass
            min_max = []
            for c in range(1, maximum+1):
                min_max.append(c) #creates the full dict up to here running correctly
                if min_max == num_positives:
                    return maximum+1
            else: #can access num_positives at this point
                for m in min_max:    
                    if m not in num_positives:
                        gap_nums.append(m)
                lowest_gap = gap_nums[0]
                return lowest_gap

print(solution([1, 3, 6, 4, 1, 2])) #5
print(solution([1, 2, 3])) #4
print(solution([-1, -3])) #1


