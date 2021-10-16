'''continue skips only particular iteration and continues the loop
  pass= ...
  
'''
#pass
class define():
    pass
    #it is like PLACE HOLDER
    #IT CONTAINS NULL VALUE
 
#with continue:
num=[10,20,30,0,50,0,60]
# python pvm wil stop execution after getting error at zero
#we need to manage abnormal termination so we use
# continue or exception handling concepts
for n in num:
    if n==0:
        print('how u can expect value from divide with zero ')
        continue
    print('100/{}={}'.format(n,100/n) )
    

# with out continue
# python pvm wil stop execution after getting error at zero
num=[10,20,30,0,50,60]
for n in num:
    print('100/{}={}'.format(n,100/n))
