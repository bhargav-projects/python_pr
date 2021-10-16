
#finding squares using map
print(list(map(lambda x:x**2,range(10))))

print( [x**2 for x in [1,3,6,10]])

squares=[]
for i in range(10):
    squares.append(i*i)
print(squares)

squares=[i*i for i in range (10)]
print(squares)

#map function to
x=1,2,3,4,5,6,7,8
print(tuple(map(lambda x:x**2,x)))

x=1,2,3,4,5,6,7,8
print(list(map(lambda x:x**2,x)))
