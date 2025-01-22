import time

my_dict = {}

def some_function(n):
    if n in my_dict:
        return my_dict[n]
    
    print(f'Computing the result for {n}')
    time.sleep(1)
    res=n**3
    my_dict[n] = res
    return res

print(some_function(4))
print(some_function(5))
print(some_function(7))
print(some_function(4))
print(some_function(14))