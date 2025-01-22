name ='Shetty'
print(name[0:-1])
name.count
first = 'Keerthan'

print(f'{first} [{name}] is a coder')

print(name.__eq__("ll"))

def cou(n):
    d = {}
    l = []
    for i in n:
        if i not in d:
            d[i] = n.count(i) 
        l.append((i, d[i]))
    return d, l

print(cou(first))

print(name.title())

for i in range(5):
    print(i* '*')



n = 5  # Number of rows

for i in range(1, n ):
    print(' ' * (n - i) + '*' * (2 * i - 1))

i=0
while i<1:
    num=int(input("Guess : "))
    if num==9:
        print(f'Hurray, it is {num}')
        break
    i+=1
else:
    print("Out of Luck")

lis = [1,3,4,6,6,2,3]
for i in lis:
    if lis.count(i)>1:
        lis.remove(i)


print(lis)