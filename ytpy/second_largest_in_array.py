list1=[0,1,2,5,4]
first_max = max(list1[0],list1[1])
second_max = min(list1[0],list1[1])
list1_length = len(list1) # length required to check upto length of input interbale

for number in range(2,list1_length):

    # checking and swapping first_max and second max
    if list1[number] > first_max:

        # assgining first max value to second max 
        # because list ele value greater than first max
        second_max = first_max
        first_max = list1[number]

    # if ele greater second max and not equal to first max
    elif list1[number] > second_max and  list1[number] != first_max :
        second_max = list1[number]

print('first max:{} - second max:{}:'.format(first_max,second_max))

# time complexity
for first in range(list1_length):
    for second in range(first+1,list1_length):
        if list1[first]>list1[second]:
            list1[first], list1[second] = list1[second], list1[first] 
print(list1[-2])

def get_second_largest(array):

    largest = 0
    second_largest = 0

    for number in array:

        if number > largest:

            second_largest = first_max
            first_max = number

        elif number > second_largest and number != second_largest:
            second_largest = number

    return second_largest


def get_second_largest(array):

    largest = max(array[0], array[1])
    second_largest = min(array[0], array[1])

    for number in array[2:]:

        if number > largest:

            second_largest = first_max
            first_max = number

        elif number > second_largest and number != second_largest:
            second_largest = number

    return second_largest



def get_second_largest(array):
    return max( filter(lambda x: x != max(array), array), default="2 elements required.")