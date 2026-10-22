def log_deco(func):
    def wrap(*args, **kwargs):
        print("values ", args)
        result = func(*args)
        print("Result: ", result)
        return result
    return wrap

def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return wrap

@log_deco
@greater_first
def sub(a,b):
    return a-b

@log_deco
@greater_first
def divide(a,b):
    return a/b

@log_deco
def add(a,b,c):
    return a + b + c

#sub = greater_first(sub)
#divide = greater_first(divide)

result1 = divide(2,4)
print(result1)

result2 = sub(3,6)
print(result2)

result3 = add(4,8,3)
print(result3)
