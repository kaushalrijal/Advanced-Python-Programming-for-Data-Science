# program to display multiplication table of a  number passed via command line

import sys

n = int(sys.argv[1])

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")