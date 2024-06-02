import random
# x=input('user enter how many digits u want')
# str='cwcbjhbvksdjbvlsjdbvjhdbsvilushlvihbe'
# Pw='-'.join(random.sample(str,x))
# print (Pw)

# list=[1,2,3,4,5,6,7,8,9]
# print(random.sample(list,3))

# tuple=('hi','bhargav','ur','height')
# print(random.sample(tuple,2))


# set={'hi','bhargav','ur','height'}
# print(random.sample(sorted(set),2))


# tuple=('hi','bhargav','ur','height')
# print(random.sample(tuple,2))


# str='cwcbjhbvksdjbvlsjdbvjhdbsvilushlvihbe'
# Pw='-'.join(random.sample(str,4))
# print (Pw)

#password generator:
import random
def pg1():
    lowerchars=['a','b','c']
    upperchars=['A','B','C']
    numericchars=['1','2','4']
    specialchars=['@','!','$']
    
    pg=random.choice(lowerchars)+random.choice(upperchars)+random.choice(numericchars)+random.choice(specialchars)
    print(pg)
pg1()
