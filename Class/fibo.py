import sys

n = int(sys.argv[1])


a = 0
b = 1
for i in range(1, n+1):
    c = a+b
    a = b
    b = c

print(f"{n}th fibonacci term is {c}")