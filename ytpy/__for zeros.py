n1=100_000_000  #underscore for easy under statnding
n2=100_000_000
tot=n1+n2
print(f'{tot:,}')

def fib():
    a,b=0,1
    while True:
        yield a
        print(a,end=' ')
        a,b=b,a+b
for i in fib():
    if i >20:
        break
fib()