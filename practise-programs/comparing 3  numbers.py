
#with out split we get confusion and all values will be combined 
a,b,c=input('enter  3 numbers ').split(',')
print('max number is :',( a if a>b else b if b>c else c)) 
 
#eval is the best method all the time
#user input = [1,2,3]or (1,2,3) or set{1,2,3}
a,b,c=eval(input('enter 3 numbers'))
print(a if a>c else c)if a>b else b

#map 
a,b,c=map(int,input('enter 3 numbers').split(' '))
print('max number is :',(a if a>b else( b if b>c else c)))  

#function
def big(a,b,c):
    return (a if a>b else b if b>c else c)  #return always give boolen values
print(big(2,3,4))

a,b=2,30
print( a,"is big") if a > b else print(b," is big")

a,b,c=[int(x) for x in input('enter 3 numbers ').split(',')]
print('the sum is :',a+b)