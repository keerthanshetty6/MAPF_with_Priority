def decorator_fn(fn):
    def wrapper_fn(*mas):
        print("I am the wrapper fn before eg")
        return fn(*mas)
    return wrapper_fn

def eg(msg):
    print(f"{msg},I ran")

eg('Hi')
dec=decorator_fn(eg)
dec('Hi')

print('with decorators')

@decorator_fn
def eg_dec():
    print("I ran")

eg_dec()


#@decorator_fn same saying -->  fn = decorator_fn(fn)

def decorator_fn(fn):
    def wrapper_fn(*args,**kwargs):
        print("This is the wrapper function part \n")
        fn(*args,**kwargs)
        print(f'After executing the function {fn.__name__}\n')
    
    return wrapper_fn

@decorator_fn
def say_hello(fname,lname):
    print(f'Hello, {fname} {lname}, Welcome')


@decorator_fn
def say_hi():
    print('Hello, Welcome')

say_hello("Kee","She")
say_hi()

#decorators replaces the decorated fn with the wrapper fn


class decorator_class:
    def __init__(self,fn):
        self.fn=fn

    def __call__(slef,*args,**kwargs):
        print("This is the call function part \n")
        slef.fn(*args,**kwargs)
        print(f'After executing the function {slef.fn.__name__}\n')


@decorator_class
def say_hello(fname,lname):
    print(f'Hello, {fname} {lname}, Welcome')


@decorator_class
def say_hi():
    print('Hello, Welcome')

say_hello('Keerthan','Shetty')
say_hi()


#if not using @decorator_class
#decorated_greet = decorator_class(say_hello)  # Manually instantiate the decorator
#decorated_greet("Alice","aa")  # Call the decorated function
