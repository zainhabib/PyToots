x = [12, 64, 29, 90, 231, 59, 75, 5, 98, 45, 8, 12, 0]
#     0   1   2   3   4    5   6  7   8   9  10 11  12 
print(f"x = {x}, type={type(x)}") # Type is 'list'

print(f"Number of elements in the list (len(x)) = {len(x)}") # len is short for length

print(f"First index is 0. x[0] =  {x[0]}")
print(f"7th item is Sixth index is 6. x[6] =  {x[6]}")
print(f"Get the last item x[-1] = {x[-1]}")
print(f"Get the third to last item x[-3] = {x[-3]}")

### Slicing
#firstThree = x[0:3]
print(f"First three items of x is x[0:3] = {x[0:3]}")
print(f"OR First three items of x is x[:3] = {x[:3]}")

#lastThree = x[-3:]
print(f"Last three items of x is x[-3:] = {x[-3:]}")

thirdToSixth = x[3:7]
print(f"third to sixth items x[3:7] = {x[3:7]}")

# Add new item to the end of x list
x.append(83)
print(f"After adding 83 x is {x}")