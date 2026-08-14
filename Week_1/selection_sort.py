# This is a simple implementation of selection sort in Python
'''
State
-----
i : ordered elements

j : current compared element

minIndex : smallest element found so far

Invariant
---------
After every outer loop iteration, ordered_arr contains exactly the smallest i elements of the original array, in sorted order.
'''

# In this implementation we create a seperated ordered array
def selection_sort1(arr):
    ordered_arr = []
    # i is for how many numbers we ordered so far in new array
    for i in range (0, len(arr)):
        minIndex = 0
        # j is for which index we're comparing
        for j in range (1, len(arr)):
            # if current index's value is smaller than our previous smaller value, we make the new smallest
            if(arr[minIndex]>arr[j]):
                minIndex= j
        ordered_arr.append(arr.pop(minIndex))
    
    return ordered_arr

unordered_arr1=[8, 12, 5, 1, -5]
print(selection_sort1(unordered_arr1))

# In this implementation we swap the minIndex with the 0th index
def selection_sort2(arr):
    for i in range (0, len(arr)):
        minIndex = i
        for j in range (i+1, len(arr)):
            if(arr[minIndex]>arr[j]):
                minIndex = j
        # Swapping 
        """
        a= arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = a
        """
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
unordered_arr2= [8,12,5,1,-5]
print(selection_sort2(unordered_arr2))

'''
What is it's correction?
After each outher iteration, the first i elements are the smallest i elements of the original array and they are in sorted order. 

Time Complexity : O(n^2)
Space complexity for first version: O(n)
Space complexity for second version: O(1)
'''