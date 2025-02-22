# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Step 1: Calculate the total sum of the array
    total_sum = sum(A)
    
    # Step 2: Initialize variables for tracking the minimum difference and left sum
    min_diff = float('inf')  # Start with infinity as the initial minimum difference
    sum_left = 0             # Sum of the left part
    
    # Step 3: Iterate through the array to find the minimal difference
    for i in range(1, len(A)):  # P can be from 1 to N-1
        # Add the current element to the left sum
        sum_left += A[i - 1]
        
        # Calculate the right sum
        sum_right = total_sum - sum_left
        
        # Calculate the absolute difference
        diff = abs(sum_left - sum_right)
        
        # Update the minimum difference if the current one is smaller
        min_diff = min(min_diff, diff)
    
    # Step 4: Return the minimal difference
    return min_diff
