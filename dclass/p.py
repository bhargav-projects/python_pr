


data=[1,2,3,4,5]
for i in data:
    if i<0:
        data[i]=0
    elif i.isupper():
        data[i]=i.upper()
print(data)
