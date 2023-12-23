def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers   

    """
    #if list of integers is empty
    if ints == []:
        return (None,None)
    
    min_elem = ints[0]
    max_elem = ints[0]
        
    #single traversal
    for elem in ints[1:]:
        if min_elem > elem:
            min_elem = elem
        if max_elem < elem:
            max_elem = elem
            
    return (min_elem,max_elem)

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


### Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


## My test cases:

##Test case1(empty):


l = [i for i in range(0, 0)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

##Test case2(very large):

l = [i for i in range(3, 10000004)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((3, 10000003) == get_min_max(l)) else "Fail")


## Test case3:


l = [i for i in range(-100, 200)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((-100,199) == get_min_max(l)) else "Fail")




# ### Time complexity:
# <br>This algorithm has a time complexity of O(n), where n is the number of elements in the list. 
# <br>It performs a single traversal through the list, updating the minimum and maximum elements.
# <br> This approach is both simple and efficient for finding both the minimum and maximum elements with a linear scan and asked/required time complexity of O(n).

# ### Space complexity:
# <br> = is O(1), which is constant. 
# <br> - The reason for this is that the algorithm uses a fixed number of variables (min_element and max_element) to store the current minimum and maximum values. The space required does not depend on the size of the input list
# <br> - it remains constant regardless of the number of elements in the list.