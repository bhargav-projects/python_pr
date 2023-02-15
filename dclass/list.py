''' 
    len() is only applicable for lst,tuple,set,str,dict,range OR 
           sequence items
    except = int complex bool

    #! sorted(),reversed(),count(), these fun always returns the list format 
    #^ sort() method only applicable t0 <list objects>
    #~ we can provide KEY as parameter(using lambda x:x[0]) to pass conditon to list
    #& sorted(iterable, reverse=True) return values in descending order
 
'''
# It is returning list of str output
s="Learning Python is very very easy !!!" 
l=s.split()  #list of str output

list_object=[1,2,3]

'''
append add elements or list objects to end in list without removing square braces
append fun takes only one argument
'''
list_object.append(10) or list_object.append([1,2,3,3,43,2])
list_object.extend("bha") # ['b','h','a'] #! int(10) error


#! solve index out of range error using membership operators!
# If index is +Ve value & out of range it accepts elements to right end 
list_object.insert(100,1000)  # 1,2,3,1000

# If index is -Ve value & out of range it accepts elements to Left end 
list_object.insert(-10,1000)  # 1000,1,2,3

"""
 #! Remove elements from the list
    remove() : accept list value 
    pop()    : accept list index value
        Default  pop() will remove last value in list
        #^ if pop(index value) > len(list) :
           #!pop will throw error
"""

#list.remove(value to be removed from the list)
list_object.remove(9) 

list_object.pop() 
list_object.pop(7)

#this function works with #! <list set dict> objects
list_object.clear()

#reversing list lements
def reversing_list():
    
    list_object=[1,2,3,4,5,6]

    newlist=[]
    another_list=[]
    while l:
        temp=l.pop()
        newlist.append(temp)

    # 2nd Way    
    for value in list_object:
        another_list.insert(0,value)

reversing_list()
 
#converted to single list
a=[[10,20,30],[30,40,50],[50,60,70]]
b=[y for x in a for y in x]

# 3 varibles method 
names=['radha','krishna','guru','mahesh']
qual=['queen','king','saviour','devote']
places=['vrindav','vrindava','bulok','bulok']
for name,qual,place in zip(names,qual,places):
    f'{name} is actually {qual} from {place}'

# Enumerate is for showing index values
names=['radha','krishna','guru','mahesh']
qualities=['queen','king','saviour','devote']
for index,name in enumerate(names):
    qual=qualities[index]   # here the change is saperatedly specify the index with defined varible
    print(qual)

#! If step value is 0 in forward direrection(L to R) and result is always empty
#! If step value is -1 in backward direction(R to L) here result is always empty
 
#when negative indexing #!default end : -(len(string) + 1)

#negative slicing 
s=[1,2,3,4,5,6,7,8,9]
"""
  #! here lenght of s is 9 
  # so for last element we can take that element also 
  # print(s[9]) error  -->but print(s[8]=9)
  # ^ slicing allowing the last element also like below 
  s[9:1:-1] is starting with 8,7,6...
  s[8:1:-1] here also the same 8,7,6...

"""
# s[9:1:-1]
# s[9:1:-2]
# s[8:1:-1] here it starts after 8 and it stops before 1 that is 2
# s[8:1:-2]
# s[7::-1]
# s[7::-2]
# s[-7:1:-1]
# s[8::-2]
 