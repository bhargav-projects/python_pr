# n=int(input(' enter no of rows do you want '))
# for i in range(n):
#     print('*'*n)

# * B paTTERN 
for row in range(7):
    for col in range (5):
        if (row in {0,3,6}) and (col in{0,1,2,3}):
            print('*',end=" ")
        elif (row in {1,2,3,4,5}) and (col in {0,4}):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

#p2
n=4
for k in range(n):
    print((' '*(n-k-1))+('* ')*(k+1))

##P3
#1
#2 3
#4 5 6
#7 8 9 10
n=4
c=0
for k in range(n):
    for j in range(k+1):
        c=c+1
        print(c,end=' ')
    print()

#*p4
