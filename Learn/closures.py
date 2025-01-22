def multiplier(num):

    def multiply_by(n):
        print(f'{num} multiplied by {n} is {num * n }')

    return multiply_by

val = multiplier(17)

val(5)

import math
print(math.__name__)  # Output: math (the name of the module)
print(math.__doc__)   # Output: Documentation string for the math module
print(math.__dict__)  # Output: Location of the module file
