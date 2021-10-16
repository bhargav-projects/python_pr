list1=[1,30,40,3,28,37]
mx=max(list1[0],list1[1])
secondmx=min(list1[0],list1[1])
n=len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmx=mx
        mx=list1[i]
    elif list1[i]>secondmx and mx != list1[i]:
        secondmx=list1[i]
print('second max:',str(secondmx))
            
        
