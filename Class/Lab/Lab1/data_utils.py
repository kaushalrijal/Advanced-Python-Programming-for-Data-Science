import matplotlib.pyplot as 

class DataSample:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def summary(self):
        return {
            "mean": sum(self.values)/len(self.values),
            "max": max(self.values),
            "min": min(self.values),
            "range": max(self.values)-min(self.values),
        }
    
    def mean(self, lst):
        return sum(lst)/len(lst)

    def max_value(self, lst):
        return max(lst)

    def min_value(self, lst):
        return min(lst)

    def data_range(self, lst):
        return max(lst) - min(lst)

    def variance(self, lst):
        mean_val = sum(lst)/len(lst)
        return sum((x-mean_val)**2 for x in lst)/len(lst)

    def std_dev(self, lst):
        return self.variance(lst)**0.5
    
    def display(self):
        print(f"Data Sample: {self.name}")
        print("Values:", self.values)
    
        