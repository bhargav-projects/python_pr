def subsequencFind(input_string, output_string=""):
    
   
    if len(input_string)==0:
        print(output_string,end=' ')
        return
    subsequencFind(input_string[:-1], input_string[-1]+output_string)
    subsequencFind(input_string[:-1], output_string)

    return
 
#not giving all sequences
input_string='abc'
subsequencFind(input_string)

input_string="abc"
output= []
for first_value in range(len(input_string)): 
    for second_value in range (first_value+1, len(input_string) +1):
        print (input_string [first_value: second_value]) # a,ab,abc,b …
        output. append (input_string [first_value: second_value])
print(output)
