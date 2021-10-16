''' ord() char to int 
chr() int to char

A-65---Z-90
a-97---z-122
0-48
#-34 '''

#for lower case
# s=input('enter a string')
# res=''
# for k in range(len(s)):
#     res=res+chr(ord('a')-ord(s[k])+ord('z'))
# print(res)

#for all types:
s='Abc'
res=" "
for k in s: #if we want to compare string elements 
    if k.islower():
        res+=chr(97+(122-ord(k)))
    if k.isupper():
        res+=chr(65+(90-ord(k)))
print(res)


#for k in s: if u want to comapre element use in 
#for k in range(len(s)) : this is for comapring every ele 
# in side the given obj until the length finished.