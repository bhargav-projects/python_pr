

def binary_search(array, target_value):
    
	# List should be in sorted and no duplicates 
    array = list(set(array))
	starting_index_value = 0
    ending_index_value = len(array)-1
    middle_index_value = 0
    
    while starting_index_value<=ending_index_value:
        
        middle_index_value = (ending_index_value+starting_index_value)//2
        
        # if target_value value is greater than middle_index_value ignore left half:
        if array[middle_index_value] < target_value:
            starting_index_value = middle_index_value + 1
        
        # removing right off from the middle
        elif array[middle_index_value] > target_value :
            ending_index_value = middle_index_value - 1
            
        else :
            return middle_index_value

    return -1

arr = [ 2, 3, 4, 10, 40,3,38,43,2,65,2,65,1,56,667,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,679,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4, 10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67,2, 3, 4,
        10, 40,3,23,43,2,65,2,65,1,56,67,23,7,687,2,65,79,3,34,87,32,34,67]
x = 667       
result=binary_search(arr,x)    
# result=binary_search([1,9,2,0,2,3,7,8,23,9,10],23)    
print(result)

 

