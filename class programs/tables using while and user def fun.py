def tables(n):
    for i in range(1,n+1):
        print(" table :",i)
        for j in range(1,11):
             print(i,"x",j,"=",i*j)
    return
n=int(input(" enter a range :"))
tables(n)

# without def 
for k in range(1,6):
    for j in range(1,11):
        print(k,'*',j,'=',k*j)
        print()
    print()
    

print('enter number which table u want ')
table=int(input())
for k in range(1,11):
        print(table,'*',k,'=',k*table)
        print()