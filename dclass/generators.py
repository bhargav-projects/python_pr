'''
generators is like normal function but it 
produce value one by one  by using yield keyword
3 ways of calling generator

return vs yield : return will print the particular value in inside fun 
                  and it will be in end of the function body
           but yield will allow the function to run multiple times and 
           you can use multiple yields in inside fun

#* return statement end the function but but yield not like that

*-next()
*list(result)
*for loop
generator expression=(())



'''

#for loop 
#squares
def squares():
    x=1
    while x<=10:
        sq=x*x
        yield sq
        x=x+1

squ=squares()
for x in squ:
    print(x)


#count numbers
def firstn(num):
    n=1 
    while n<=num:
        yield n
        n+=1 
values=firstn(5) 
for x in values: 
    print(x) 

#by giving n value 
def squares(n):
    x=1
    while x<=n:
        sq=x*x
        yield sq
        x=x+1

squ=squares(10)
for x in squ:
    print(x)

#NEXT 
def squares(n):
    x=1
    while x<=n:
        sq=x*x
        yield sq
        x=x+1
s=squares(10)
print(s.__next__)    # created generator obj
print(s.__next__())  # now iterator will iterate this generator obj 
print(s.__next__()) 

#LIST
def squares(n):
    x=1
    while x<=n:
        sq=x*x
        yield sq
        x=x+1
print(list[squares(10)]) #created generator obj
print(list(squares(10)))


"""
generator is a function that returns an function object 
which can iterate over  as one value at a time"""
''' iterators  are iterates every time where in lists ,tuples ,strings
and iterates takes more memory when  comared to genrators'''
# itertools ,--> map,reduce,file,zip
 

mylist=[i for i in range (10000)]
print(sum(mylist))
# Initialize the list using generator
my_list1 = [1, 3, 6, 10]
# acutually its like tupel concept but
#  there is no tuple comprhesnion in python 
# so it is called generators
a = (x**2 for x in my_list1) 
print(next(a))
print(next(a))
print(next(a))
print(next(a))
