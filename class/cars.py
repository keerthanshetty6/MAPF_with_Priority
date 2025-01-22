class car:
    def __init__(self,brand:str, horsepower:int) ->None:
        self.brand=brand
        self.horsepower=horsepower
    #dunders
    def __str__(self)->str:
        return(f'{self.brand},s={self.horsepower} hp')
    
    def __add__(self,other)->str:
        return(f'{self.brand} + {other.brand}')

bmw:car=car("BMW",180)
vw:car=car("VW",200)
print(bmw.brand)
print(bmw+vw)