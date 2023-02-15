
'''
listijk = [] #an empty list to be filled as following
for i in range(x + 1): #it will output 0, and will only output 1 after the next conditions ('for j' and 'for k') are met.
    for j in range (y + 1): #it will output 0, and will only output 1 after the next condition ('for k') is met.
        for k in range (z + 1): #it will output 0 and then 1.
            listijk.append([i,j,k]) #it will add i, j and k values to the list
print(listijk) #print the list properly filled
'''

x,y,z,n=map(int,input('enter vals with spaces').split(" ")) 
# x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(x+1) 
        for b in range(y+1)
        for c in range(z+1) 
        if a + b + c != n ])


x,y=eval(input('enter your data structure along with values'))
print (x,y)

