class Item:
    discount=0.8
    all=[]

    def __init__(self,name: str,price: float,quantity:int):

        assert price>=0,f"Price {price} is not >= 0"
        assert isinstance(quantity, int) and quantity>=0,f"Quantity {quantity} is not a positive int"

        self.name=name
        self.price=price
        self.quantity=quantity


        Item.all.append(self)

    def __repr__(self):
        return f"Item({self.name})"
    
    def cal_cost(self):
        return self.price * self.quantity
    
    def cal_discount(self):
        return self.cal_cost() *self.discount

item1=Item("Bat",32.9,11)
item1=Item("Ball",5.6,11)
item1=Item("Stumps",19,11)
print(item1.cal_discount())
print(Item.all)
