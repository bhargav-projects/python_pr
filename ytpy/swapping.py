#swapping using temp
#by using split it takes only string 
x,y=input('2numbers').split(',')
t=y,x
x,y=t
print(t)
# x,y=y,x
print(type(t)) # its tuple because it is pack and unpack concept

#type
a=2
b=3
t=a
a=b
b=t
print(a,b)

#type5
a=1
b=2
a=a+b
b=a-b
a=a-b
print(a,b)


# Type6^bit wise XOR operator
a=1
b=2
a=a^b
b=a^b
a=a^b
print(a,b)
