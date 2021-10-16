import os,sys
fname=input('enter file name')
if os.path.isfile(fname):
    print('file name exists',fname)
    f=open(fname,'r')
else:
    print(fname,'is not found')
    sys.exit(0)
lcount=wcount=ccount=0
for line in f :
    lcount+=1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)

print(' the number of lines count',lcount)
print('the number of word count',wcount)
print('the number of char count ',ccount)

    
#directory commands
import os
cwd=os.getcwd()
#mkdir(),rmdir(),mkdirs(),removedirs(),rename('old name','newname')
#pathname,pathfile,pathdir

# read an entire text file
txt = open("python.txt","r")
print("type of mode:",txt.mode)
print(txt.read())

#append text to a file and display the text
f=open("py33.txt", "a")
f.write(" today is 6-july-2021\n")
f.write("today is Tuesday \n")
f.close()

newfile = open("py33.txt", "r")
print(newfile.read())    
#find the longest words from the given text file
def longest(filename):
    with open(filename, 'r') as inline:
        words = inline.read().split()
    max_length= len(max(words, key=len))
    return [ word for word in words if len(word)==max_length]
print(longest('new2.txt'))

#2
f=open('D:\python class\programing class\sample file.txt','r')
temp=0
for line in f:
    for word in line.split():
        temp2=len(word)
        if temp2>temp:
            temp=temp2
print(f'gretest wordd is {temp} digits') 

#takes a text file as input and returns the number of words of a given text file
f=open('D:\python class\programing class\sample file.txt','r')
temp=0
for line in f:
    for word in line.split():
        temp2=len(word)
        temp=temp2+temp
print(f'number of words in file is {temp} digits')   
 
#3
file = open("abc.txt", "r")
print(file.read())
file.close()

file = open("abc.txt", "r")
count=0

words = file.read().split()
for word in words:
    count=count+1
print("No of words:",count)

#4

fname = stud.info 
num_count = 0 
with open("stud.info", 'r') as f: 
    for line in f: 
        words = line.split() 
        num_count += len(words) 
print("Number of words:",num_count)