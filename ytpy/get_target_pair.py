def get_target_pair(array, target):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        pair_sum = array[left] + array[right]

        if pair_sum == target:
            return f"Indexes are{left, right}."

        elif pair_sum < target:
            left += 1
        else:
            right -= 1

    return "No Pairs Found"


# using Complement
def get_target_pair(array, target):
    '''
    using complement approach
    2's complement is 8 
    here 2+8=10

    storing array elements as keys and its indexes are values
    and these elements we can used for comparing the apporiate elements.
    
    '''

    num_index = {}
    for index, number in enumerate(array):
        complmnt = target - number

        if complmnt in num_index:
            return [complmnt[index], index]

        num_index[complmnt] = index

    return ["", ""]


#

def get_target_pair(array, target):
    import itertools   

    for pair in itertools.combinations( range(len([1,2,3,4,5])), 2):
        if array[pair[0]] + array[pair[1]] == target:
            return pair[0], pair[1]
    
    return 0, 0