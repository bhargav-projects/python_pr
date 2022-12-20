names='radha','krishna','guru','mahesh'
places='vrindhavan','gokul','earth'

for index,name in zip(names,places):
    print(index,name)

list1=1,2,3
list2='hi','bhargav','how are you'
x=11,22,33
x1='iloveu','radhakrishna'

print(list(zip(list1,list2,x,x1)))

