
''' #*step values can be either  +ve or -ve

    for +ve indexing :
    if stop index is +ve value  the direction will be (left to right-1)
    if stop index is -ve value  the direction will be  (right to left+1)
 
    # for -ve indexing
    # if +ve   fwd dir beg to end-1
    # if -ve   fwd dir beg to end+1

    -->string spaces =lstrip,rstrip,strip
        these inbuilt functions doesn't remove any space in the string

string indexing:
    find and index both are same.
     if value not found 'find' return -1
     index return "substring not found error"
                  
   

    print(S.rfind('a')  
    # it serches from rightside to left side and if no occurence matched then it  gives  -1'
    
    print(S.rindex('a',5,len(S)) 
    # it serches from rightside and if no occurence matched then it  gives ERROR'

'''

# It is returning list of str output
s="Learning Python is very very easy !!!" 
l=s.split()  # it is returns list of string values

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
print(S.strip())  # hi bhargav
print(S.lstrip()) # hi bhargav          '
print(S.rstrip()) # '           hi bhargav

#FindingSubscripts
S5='herbkjhbsjhzgvssd'
print(S.find('a')) # find total string from left to right
print(S.find('a',5,len(S)))
print(S.rfind('z') ) # it serches from rightside and if no occurence matched then it  gives  -1'
print(S.index('a'))
print(S5.rindex('z',5,len(S)))
# it serches from rightside and if no occurence matched then it  gives ERROR
    

#finding  all occurences and  return inde
s="aabcadef"
find_ = "a"
d={}
for index,x in enumerate(s) :
  if x == find_:
    if x in d.keys():
      d[x].append(index)
    else :
      d[x] = [index]
 

# split() : this fun only works with str  
# [sep=' '] works only with inside print

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
# case fold is the strongest than .lower()
print(s.lower())
print(s.casefold())
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
  
# count repeated charcaters in str simple format 
s=input('enter repeted strchars')
d={}
for x in s:
    d[x]=d.get(x,0)+1
 
# convert word into upper and find len
words =' hi bhargav how r u '.split()
l=[[w.upper(),len(w)] for w in words ]
print(l)

s='bhargav'
k=0
for j in s:
    print('+ve indx:{} -ve index:{} value of j:{}'.format(k,k-len(s),j))
    k=k+1

 
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




















