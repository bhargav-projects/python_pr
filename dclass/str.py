
''' #*step values can be either  +ve or -ve
for +ve indexing 
if +ve  fwd dir (left to right)
if -ve   bwd  dir (right to left) #decreasing order 

for -ve indexing
if +ve   fwd dir beg to end-1
if -ve   fwd dir beg to end+1

string spaces =lstrip,rstrip,strip
these functions doesn't remove any space insdie str

string indexing:
find and index r both are same difference is only -1 if value not 

print(S.rfind('a')  # it serches from rightside and if no occurence matched then it  gives  -1'
print(S.rindex('a',5,len(S)) # it serches from rightside and if no occurence matched then it  gives ERROR'

len() is only applicable for list OR  sequence values 
#* list also packing and unpacking aplicable 
'''

# It is returning list of str output
s="Learning Python is very very easy !!!" 
print(type(s)) 
l=s.split()  # it is returning list of str output
print(l) 
print(type(l)) 
# replace str
s='hi bhargav how  r u'
#s=s.replace('bhargav','good boy')

#slicing
s='0123456789'
print('+ve index') 
print(' 1    s[::]=>exact what we definied ',s[::],'\n')

print(' 2   s[10:0:-1] => decreasing order',s[10:0:-1],'\n' )
print(' 3  nothing will print if like  this s[0:10:-1] ',s[0:10:-1],'\n' )
print(' 4 s[2:-5:1]',s[2:-5:1], ' \n 5 s[2:-5:-1] ,s[0:-5:-5]--> it wil print nothing ' ,s[2:-5:-1],s[2:-5:-5])

print('-ve index')
print('s[-1:-6:-1] => -ve slicing form right to left ',s[-1:-6:-1],'\n')
print(' nothing will print if use step as 1 s[-1:-6:1]',s[-1:-6:1])   

#striping
S='           hi bhargav           '
print(S.strip())
print(S.lstrip())
print(S.rstrip())

#FindingSubscripts
S5='herbkjhbsjhzgvssd'
print(S.find('a'))
print(S.find('a',5,len(S)))
print(S.rfind('z') ) # it serches from rightside and if no occurence matched then it  gives  -1'
print(S.index('a'))
print(S5.rindex('z',5,len(S)))# it serches from rightside and if no occurence matched then it  gives ERROR
    

#finding  all occurences and  return inde
s=input(' enter name')
subs=input('which word u need to search')
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos  == -1:
        break
    print('found at location',pos)
    flag=True
if flag==False:
    print('not found')
 
# counting no of occurences 
s1='bhargav'
print(s1.count('b'))
print(s1.count('b',2,len(s1)))
print(s.replace('bhargav','good boy'))

# split() : this fun only works with str   and [sep=' '] works only with inside print
s2='bjh dsbf gbsh bsh dv'
print(s2.split())
print(s2.split(' ',3)) # it means that only applicable for 3 spaces [this is called max split ]
print(s2.rsplit('-',3)) 
print(s2.split(','))

# join() , it works with list ,tuples  ,str
s3=['bhargav','how','r u']
print(' '.join(s3))  # if we dont pass any thing it combine everything
s3=['bhargav','how','r u']  #list
print('-'.join(s3))   
s3=('bhargav','how','r u') # tuple
print('-'.join(s3))
s3='bhargav','how','r u'    #str
print('-'.join(s3))

#changing case of string
s='Hi Bhargav Hi Ra'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())  # it changes every first letter in  words   ex:hi bhargav hi  Ra
print(s.capitalize()) # it changes only first letter in total sentence  ex:hi Bhargav Hi Ra

# checking in  str
s='hi bhargav '
print(s.startswith('hi'))
print(s.endswith('vag'))

#----------------------------------------------
print('bhargav123'.isalpha())
print('bhargav'.isalpha(),'\n')

print('bhargav123'.isalnum(),'\n')

print('bhargav123'.isdigit())
print('123'.isdigit(),'\n' )

print('6 BHARGAV123'.isupper())
print(' BHARGAV'.isupper(),'\n')

print('bhargav123'.islower())
print('bhargav'.islower(),'\n')

print('Bh Ar Gav 123'.istitle())  # its expecting first charectar alway title 
print('Bh Ar Gav '.istitle(),'\n')

print('Bh Ar Gav 123'.isspace())
print(' '.isspace())

# string reverse method
print('#type1')
s='bhargav'
print(s[::-1])

print('#type2 it gives default value')
print(reversed(s))

print('#type3')
for x in reversed(s):
    print(x)

print('#type4')
for x in reversed(s):
    print(x,end=' ')
    print( )

print('#type5')
print(' '.join(reversed(s)))


print('#type6')
i=len(s)-1
output=' '
while i>=0:
    output=output+s[i]
    i=i-1
print(output)


print('#type7') # its no working 

i=len(s)-1
l=[]
while i>=0:
    l.append(s[i])
    i=i-1

print(' '.join(l))


# __print even and odd positions in str 
s4='12345678901234'
i=0
while i<len(s4):
    print('all even positions ')
    print(s[i],end=' ,')
    i=i+2
print()

i=1
while i<len(s4):
    print('all odd positions ')
    print(s[i],end=' ,')
    i=i+2
    
# sorting given  num and char in str
s=input('enter a value ')
s1=s2=output=' '
for x in s:
    if s.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output +=x
for x in sorted(s2):
    output +=x
print(output)

#wap to display the char with given number of times 
s5=input('enter letter which u want print times')
op=' '
for x in s5:
    if x.isalpha():
        op=op+x
        prevval=x
    else:
        op=op+prevval*(int(x)-1)
print(op)


#every start char will get reult of next  chars of givennumber
s5=input('enter string with numbers')
op=' '
for x in s5:
    if x.isalpha():
        op=op+x
        prevval=x
    else:
        newch=chr(ord(prevval)+int(x))
        op=op+newch
print(op)


#every start char will get reult of next  chars of givennumber
s5=input('enter 1 string ')
s6=input('enter  2 string ')

op=' '
i=j=0
while i<len(s5) or  j<len(s6):
    op=op+s5[i]+s6[j] # getting error because different length
    i+=1
    j+=1
print(op)



# for differenrt len strings
s5=input('enter 1 string ')
s6=input('enter  2 string ')
i=j=0
op=' '
while i<len(s5) or j<len(s6):
    if i<len(s5):
        op=op+s5[i]
        i=i+1
    if j<len(s6):
        op=op+s6[j]
        j=j+1
print(op)

# neglect repeated charcaters in str
s=input('enter repeted strchars')
l=[]
for x in s:
    if x not in l:
        l.append(x)

print( ''.join(l))

# neglect repeated charcaters in str simple format 
s=input('enter repeted strchars')
print(''.join(set(s)))  # here set doest nit follow order so we get different order everytime

# count repeated charcaters in str simple format 
s=input('enter repeted strchars')
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for k,v in d.keys:
    print('{} occurs{}times '.format(k,v))


#found vowels in str 

s=input("enter a word contain vowels ")
vowels=['a','e','i','o','u','A','E','I','O','U ']
found=[]
for letter in s:
    if letter in vowels :
        if letter not in found:
            found.append(letter)
print(found) # it returns list of letters 
#print(''.join(found)) # it returns normal type 
s="PYTHON is best LANG"
count=0
for x in s:
	if x in "[aeiouAEIOU]":
		count+=1
print(count)



# convert word into upper and find len
words =' hi bhargav how r u '.split()
print(words)
l=[[w.upper(),len(w)] for w in words ]
print(l)

s='bhargav'
k=0
for j in s:
    print('+ve indx:{} -ve index:{} value of j:{}'.format(k,k-len(s),j))
    k=k+1

#LOWER AND UPPER
#print lower and upper letters in given input
s=input('enter name')
lwr=[]
upr=[]
for letter in s:
    if letter.islower()==True :
        lwr.append(letter)
    else:
        upr.append(letter)
print('lwr:',lwr, 'upr:',upr)
#sentence representation types
def f1():
    s='this is python"s class'
    print(s)
    s='this is python\'s class'
    print(s)
    #double quotes
    s="this is python's class"
    print(s)
    s="this is python'''s class"
    print(s)
    s="this is python\'s class"
    print(s)
    s="this is python\''s class"
    print(s)
    s="this is python\'''s class"
    print(s)
    s="this is python\\'s class"
    print(s)
    s="this is python\\''s class"
    print(s)
    s="this is python\\\'''s class"
    print(s)
     #triple quotes
    s='''this is python\\'s class'''
    print(s)
    s='''this is python\\''s class'''
    print(s)
    s='''this is python\\\'''s class'''
    print(s)
    s='''this is python''s class'''
    print(s)
    s='''this is python's class'''
    print(s)


f1()
#getting lines 
str='''
    hi
    bhar
    gav
'''
l3=str.splitlines()[2]
print(l3)




















