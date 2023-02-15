
#! Reverse a list
  #^ using pop to get the last value store to new variable

l=[1,2,3,4,5,6]
newlist=[]
while l:
    newlist.append(l.pop())
print(newlist)

#! Push zeros to end  
  #^ using append to push non-zeros checking zeros count and 
  #^ using extend to push the zeros
input_list = [1,2,5,0,2,4,0,8,0,3,5,7,0,0,2]
output = []
count = int()
for value in input:
  if value == 0:
    count+=1
  else:
    output.append(value)
output.extend([0]*count)
print("final list after pushing zeros to end:", output)

# remove special characters and place special characters in between characters 
input_str = "%%%%Bhargav%%%Ch%%%m"
output_str = "Bhargav%Ch%m"

list2 = []
new_str = ""
for char in input_str:
    if char.isalpha():
        new_str+=char
    else:
        if len(new_str) > 0 or char == input_str[-1] :
            list2.append(new_str)
        else:
            new_str=''

print(list2)

#! Insert data into a string
'''
    Approaches:
        1.#^ slicing  
            Ex: str[0:2] + "value to be inserted" or str(value) + str[2:]
        2.#^ %d operator  (based on datatype we can change %d,%f,%s)
            Ex:  (input_str[:4] + "%d" + input_str[4:]) %7
              :  'hanning(%d).pdf' % 123
        3.#^ format()
            Ex: res = "{}{}{}".format(input_str[:4], value_to_be_inserted, input_str[:4])
        5.#^ f-strings
            Ex: var = f"this is {value} inserted" 
        4.#^ * <-- this operator
            *Ex: inp_list = ['1','bhargav','good']
            -->  *inp_list

'''
