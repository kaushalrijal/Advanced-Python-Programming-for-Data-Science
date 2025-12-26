
def simple_interest(p, t, r):
    return (p*t*r)/100

def compound_interest(p, t, r):
    return p*(1 + (r/100))**t - p

if __name__ == "__main__":
    p = float(input("Enter principal: "))
    t = float(input("Enter time: "))
    r = float(input("Enter rate:"))
    print(f"Simple Interest: {simple_interest(p, t, r):.3f}")
    print(f"Compound Interest: {compound_interest(p, t, r):.3f}")
