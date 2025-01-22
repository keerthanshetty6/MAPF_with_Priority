def cube(x):
    return x**3

a=cube(4) # () means calling or executing the fn

b=cube #first class fn -> assign fn to a variable
print(f'value of a is {a}, b(4) is {b(4)}')

#A higher order function : does the below
# 1.pass fn as arguments
# 2.return fn from another function

#1
def exp(fn,arr : list) -> list:
    res=[]
    for i in arr:
        res.append(fn(i))
    return res

arr= [x for x in range(1,11)]

print(f'The array is {arr} \nIts cube is {exp(cube,arr)} \nUsing map {list(map(cube,arr))}')

#2

def display(mesg):

    def show():
        print(f'Message : {mesg}')
    
    return show

hello=display('Hi')
print(hello)
print(hello())
hello()
print(display('Bye'))
print(display('Bye')())


def base(bas):

    def power(num):
        print(f'{bas} to the power of {num} is {bas ** num}')
    
    return power

val = base(2)
for i in range(13):
    val(i)
