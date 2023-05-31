print("Hello, World!")

x=12
# Print out value of x, type of x
print(f"x = {x}, type={type(x)}") # int=Integer

x=12.57
print(f"x = {x}, type={type(x)}") # float=float

x="Braeden and Isaac"
print(f"x = {x}, type={type(x)}") # str=String

x=False
print(f"x = {x}, type={type(x)}") # bool=boolean

x=4/2
print(f"x = {x}, type={type(x)}") # division answer is always a float

x=2*3
print(f"x = {x}, type={type(x)}") # Multiplication of two ints will be an int

x=1.1 * 2
print(f"x = {x}, type={type(x)}") # Multiplication of at least one flot will result in float

x=2+7
print(f"x = {x}, type={type(x)}") # same as multiplication

x=3.4+1
print(f"x = {x}, type={type(x)}") # same as multiplication


x = 4
y = 3
print(f"Is x = y? {x == y}, Type of result {type(x == y)}")
print(f"Is x greater than y? {x > y}")
print(f"Is x smaller than y? {x < y}")

# NO EQUAL TEST
if (x != y):
    print (f"x is not equal to y")