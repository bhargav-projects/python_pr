
# reverse a list
input_list = [1,9,30,7,2,4,6,12,7,8,32,8,22,6,89,22]
input_list_2 = [11,9,30,71,2,41,6,12,7,8,32,18,22,16,9,22]

print([*{*input_list}])

# Possibilities of 3 elements sum to target value
input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print([
    (x,y,z) for x in input for y in input for z in input if x+y+z==6
])

# removing empty strings and showing data
print(list(filter(None,input_list)))

# common elements from two objects:"
print(list(filter(lambda value:value in input_list,input_list_2)))

# tuple and objects  without using any varible using *
print(*(value for value in range(10)))


"""
If we declare any data based on values closed like {,[,(,)]} 
  they exihibit the its property 
  {} ==> it executes sets property
  [] ==> it executes list property
  () ==> it executes tuple property
"""
#! remove duplicates in the object
str_input = "jajnjcsdbcjhsaxakjakcjkads"
list_ = [1, 1, 1, 1, 23, 3, 4, 2, 233]

# Here i observed converting input to set using {}
print({*str_input}, {*list_})

"""
    If you want to filter unique elements(removing duplicate elements) in two objects
    (i.e like different iterables)
    like any datatype(list,tuple,str).
"""
l1 = [1, 2, 3]
l2 = [2, 3]
print({*l1, *l2})


"""
    we can iterate function object like 
    how we iterate iterables and map object using --> `*`
    * these operator best used for generators & normal functions too
"""
def sub_sum(a, b): return f"sum is {a+b}"


print(*sub_sum(10, 2))


def g(n):  # * operator on generator to yield all values
    for va in range(n):
        yield va


print(*g(10))

'''
 #! filter(condition,iterables)
    ---> In the place of condition you can pass lambda, datatype, function. 
'''
 
#/ In lambda fsyntax #!else is mandatory when you use IF condtion   