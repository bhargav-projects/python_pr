"""
    zip() function creates an iterator(tuple) that will aggregate elements from two or more iterables
         * zip function returns an iterator of tuples

       If the passed iterators have different lengths,
       the iterator with the least items decides the length of the new iterator

"""

list1=1,2,3
list2='hi','bhargav','how are you'
x=11,22,33
x1='iloveu','radhakrishna'

# converts to tuple object
# [(1, 'hi', 11, 'iloveu'), (2, 'bhargav', 22, 'radhakrishna')]
print(list(zip(list1,list2,x,x1))) 

# If single iterable in zip ==> tuples
values = [1,2,3,4,5]
for val in zip(values):
    print(val) # (1,)


# If combine multiple iterable in zip ==> string
names=['hi','how r u','bharg']
values = [1,2,3,4,5]
cities = "bangalore","hyd"

for val,names,citi in zip(values,names, cities):
    print(val,names, citi) # 1 hi bangalore



