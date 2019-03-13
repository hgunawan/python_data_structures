def binary_search0(input_array, value):
    """Your code goes here."""
    length = len(input_array)/2
    current_index = length
    while length > 0:
        length = length/2
        # print(current_index)                
        current_value = input_array[current_index]
        if(current_value==value):
            return current_value
        elif(current_value<value):
            # print("+")
            current_index+=length
        elif(current_value>value):
            # print("-")
            current_index-=length
    
    return -1


def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array)-1

    while low <= high:
        mid = (low+high)//2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low=mid+1
        else:
            high=mid-1
            
    return -1    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))