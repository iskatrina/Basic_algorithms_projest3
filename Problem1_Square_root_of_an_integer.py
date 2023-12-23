import pandas as pd

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
       
    """

    if number < 0:
        return None
    
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    result = 1
    for i in range(1,int(number)):
        if number >= i**2:
            result = i
        else:
            
            return result
           
## The time complexity of my first sqrt function is O(n)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
       
    """

    if number < 0:
        return None
    
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    start = 1
    end = number
    
    
    while start <= end:
        mid_element = (start + end)// 2
    
        if number == mid_element * mid_element:
            result = mid_element
            return result
        elif number > mid_element * mid_element:
            start = mid_element + 1
            result = mid_element
        elif number < mid_element * mid_element:
            end = mid_element - 1
            #result = mid_element
            
    return result
## The time complexity of mysecond sqrt function is O(log(n))
## Space complexity: O(1)

print ("Pass" if  (3 == sqrt(9)) else "Fail")

print ("Pass" if  (0 == sqrt(0)) else "Fail")

print ("Pass" if  (4 == sqrt(16)) else "Fail")

print ("Pass" if  (1 == sqrt(1)) else "Fail")

print ("Pass" if  (5 == sqrt(27)) else "Fail")

#My Test cases :
#Case1:
import math
print ("Pass" if  (int(math.sqrt(1000000)) == sqrt(1000000)) else "Fail")

#Case2:
print ("Pass" if  (int(math.sqrt(10000000000000)) == sqrt(10000000000000)) else "Fail")


#case3:
print ("Pass" if  (int(math.sqrt(1000000000000000000000)) == sqrt(1000000000000000000000)) else "Fail")

#Case4:
import math
print ("Pass" if  (int(math.sqrt(0)) == sqrt(0)) else "Fail")

    