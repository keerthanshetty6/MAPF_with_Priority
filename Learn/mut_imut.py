a='Keerthan Shetty'
print(id(a))
a="nana"
print(id(a))


lis = [i for i in range(1,10,2)]
print(lis)
print(id(lis))

lis[0] = 100
print(lis)
print(id(lis))