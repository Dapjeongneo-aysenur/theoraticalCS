## This is a simple implementation of binary search in Python

"""
State
-----
left : the left border of solution space
right : the right border of solution space
mid : the mid element in the solution space

Invariant
---------
If target exist in the array, it's always between left and right 
"""

def binary_search(arr, target):
    # If we assume the numbers will be aligned from smaller to bigger, our smallest element will be in 0th index
    left = 0
    right = len(arr) -1

    while left <= right :

        mid = (left + right) // 2

        if(arr[mid]<target):
            # 0-mid values are already smaller
            left = mid +1
        elif(arr[mid]>target):
            # mid-right values are already bigger
            right = mid -1
        else:
            # yess, we found it
            return mid
    
    # there is not such thing
    return -1

numbers = [2, 5, 7, 9, 12, 18, 24]

print(binary_search(numbers, 24))

"""
What is it's correction? 
At each iteration, we remove only the half that cannot contain the target. Therefore, if the target existed, we never discard it. Eventually either we find the target or the search space becomes empty.

Time Complexity : O(log n)
Space Complexity : O(1)

"""