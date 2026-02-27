def cubes(n):
    for i in range(n):
        yield n**3

print(next(cubes(5)))