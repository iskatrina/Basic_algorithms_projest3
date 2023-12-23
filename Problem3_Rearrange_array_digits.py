def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
       
    """
    # Sort the array using merge sort
    merge_sort(arr)

    # Create two numbers by combining alternate elements in reverse order
    num1, num2 = 0, 0
    for i, num in enumerate(arr):
        if i % 2 == 0:
            num1 = num1 * 10 + num
        else:
            num2 = num2 * 10 + num

    return [num1, num2]

    
    
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    
print(merge_sort(arr=[9,3,1,1,2,3,4,7]))
mergesort([9,3,1,1,2,3,4,7])




def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])



test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


test_function([[1,2,3,4,5], [964, 852]])
rearrange_digits([1,2,3,4,5])

## My test cases:

### test case1(empty):
test_function([[], []])


### test case2(very large):
test2 = [i for i in range(1,1000)]
rearrange_digits(test2)

### Test case3:
test3 = [23,65,3,7,8,9,2]
rearrange_digits(test3)


