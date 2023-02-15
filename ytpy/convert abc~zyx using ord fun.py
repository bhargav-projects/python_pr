''' #! ord() char to int 
    #^ chr() int to char

A-65---Z-90
a-97---z-122
0-48
#-34 '''

# for lower case
s=input('enter a string')
res=''
for k in range(len(s)):
    res=res+chr(ord('a')-ord(s[k])+ord('z'))
print(res)

#for all types:
s='Abc'
res=""
for k in s: 
    """
    If we are accessing every element in iterable object 
    We can perform mutiple opertaoins
    --> comparing one value with another
    --> converting one-another
    --> previous value and forther value comparison
    --> mutiple operations
    """
    if k.islower():
        ''' '''
        res+=chr(97+(122-ord(k)))
    if k.isupper():
        ''' '''
        res+=chr(65+(90-ord(k)))
print(res)


#for k in s: if u want to comapre element use in 
#for k in range(len(s)) : this is for comapring every ele 
# in side the given obj until the length finished.