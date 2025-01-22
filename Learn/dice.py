import random
from pathlib import Path

class dice:
    def roll():
        return random.randint(1,6),random.randint(1,6)

#inst=dice()
#print(dice.roll())

p=Path("Learn")
for file in p.glob('*.py'):
    print(file)
#print([x for x in p.iterdir()])