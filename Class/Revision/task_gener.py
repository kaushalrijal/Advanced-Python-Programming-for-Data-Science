# write a generator that yields fibonacci sequence upto n terms
def fibo(n):
    a=0
    b=1
    for i in range(n):
        c = a
        a = b
        b = c + b
        yield c

for i in fibo(15):
    print(i)