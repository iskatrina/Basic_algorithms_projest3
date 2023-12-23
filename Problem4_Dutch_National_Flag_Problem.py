def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    #using three pointers (next_pos_0, next_pos_2, and front_index) to keep track of the positions of 0s, 1s, and 2s
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    front_index = 0
 
    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            #print('==0',input_list)
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        
        elif input_list[front_index] == 2: 
            #print('==2',input_list)
            input_list[front_index] =input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        
        else:
            #print('==1',input_list)
            front_index += 1
            

    return input_list


sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
 
    
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])



## My own test cases:
### Test case1(empty):

test_function([])

### Test case2(very large):
import random

case2 = [0, 1, 2] * 300000
random.shuffle(case2)
test_function(case2)

### Test case3(missing 0):

case3 = [1,2] * 8

test_function(case3)


