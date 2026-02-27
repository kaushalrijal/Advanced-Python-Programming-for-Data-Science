def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func, __name__}")
        result = func(*args, **kwargs)
        print("Function Completed")
        return result
    
    return wrapper

@logger
def add(a, b):
    return a + b