# from module import *
# from module import simple_interest, compound_interest
import module

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate:"))
print(f"Simple Interest: {module.simple_interest(p, t, r):.3f}")
print(f"Compound Interest: {module.compound_interest(p, t, r):.3f}")