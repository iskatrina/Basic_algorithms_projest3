def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    if input_list  == []:
        return -1
    
    start = 0
    end = len(input_list)-1
    
    while start <= end:
        mid = (start + end) // 2
        
        if input_list[mid] == number:
            return mid
        
        if input_list[start] <= input_list[mid]:
            if input_list[start] <= number <= input_list[mid-1]:
                end = mid - 1
            else:
                start = start + 1
                
        else:
            if input_list[mid] <= number <= input_list[end]:
                start = mid+1
            else:
                end = mid-1

    
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


        
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


## my test cases:
### Test Case1(empty):
test_function([[], 10])

### Test Case2(first element in array):
test_function([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 1])

### Test Case3(very large array):
arr = [i for i in  range(0,1000000000)]
number = 1000000003
test_function([arr, 1000000002])



