def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper
    
def add(a, b):
    return a + b

add_int = toint(add)

print(add_int(*input().split()))