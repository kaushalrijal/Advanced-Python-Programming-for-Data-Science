"""
HOEWORK: WAP TO CREATE A CLASS NAME DISTANCE WHICH HAS FEET AND INCHES AS DATA MEMBER. OVERLOAD ANY TWO OPERATORS
""" 

class NegativeValueError(Exception):
    pass

class Distance: 
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self) -> str:
        return f"{self.feet}ft {self.inches}in"
    
    def __add__(self, other:"Distance")->"Distance":
        ic = self.inches + other.inches
        ft = self.feet + other.feet
        if ic > 12:
            ft += 1
            ic = ic % 12
        return Distance(ft, ic)

    def __sub__(self, other:"Distance")->"Distance":
        if self.feet < other.feet or (self.feet == other.feet and self.inches < other.inches):
            raise NegativeValueError("Left Operand cannot be smaller than Right Operand")
        
        ft = self.feet - other.feet
        ic = self.inches - other.inches
        if ic < 0:
            ft -= 1
            ic += 12

        return Distance(ft, ic)

d1 = Distance(5, 9)
d2 = Distance(5, 8)

d3 = d1 - d2
print(d3)

