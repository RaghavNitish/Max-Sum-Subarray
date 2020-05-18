# =============================================================================
# Data Structures and Algorithms Nanodegree Udacity (Arrays Challenges)
# 
# Problem Statement:
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within 
# the input array.
# 
# Here is an example:
# arr = [1, 2, -5, -4, 1, 6]
# output = 7 (the sum of the last two elements of the array.)
# =============================================================================

#My code
def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    largest_sum = 0
    
    while arr != []:
        if optimal_sum(arr) > largest_sum:
            largest_sum = optimal_sum(arr)
        
        if len(arr) > 1:
            arr.pop(0)
            arr.pop()
        elif len(arr) == 1:
            arr.pop()
            
    return largest_sum
    
#My code         
def optimal_sum(arr):
    largest_sum = 0
    
    #Finding largest sum in forward direction
    for i in range(len(arr)+1):
        if sum(arr[0:i]) > largest_sum:
            largest_sum = sum(arr[0:i])
    
    rev_arr = list(reversed(arr))
    
    #Find largest sum in reverse direction
    for j in range(len(rev_arr)):
        if sum(rev_arr[0:j]) > largest_sum:
            largest_sum = sum(rev_arr[0:j])
    
    return largest_sum

#helper function for testing purpose
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# =============================================================================
# Test 1
# 
# arr= [1, 2, 3, -4, 6]
# solution= 8 # sum of array
# test_case = [arr, solution]
# test_function(test_case)
# 
# Test 2
# 
# arr = [1, 2, -5, -4, 1, 6]
# solution = 7   # sum of last two elements
# test_case = [arr, solution]
# test_function(test_case)
# 
# Test 3
# 
# arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
# solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
# test_case = [arr, solution]
# test_function(test_case)
# =============================================================================
