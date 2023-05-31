x = 99
y = 1

## if -- elif -- else
if (x == y):
    print("x is equal to y")
elif (x < y):
    print("x is smaller than y")
elif (x > y): # This is true ...
   print("x is greater than y") # ... so exit the if - elif - else block after executing this
elif (x == 99): ## will not execute
    print("x is 99")
else:
    print("I have no clue")


aList = [4, 3, 56, 87, 1, 57, 12, 74, 254]
print(f"aList = {aList}")

## for
r = range(1, 10)
for i in r:
    pass
    #print(f"i = {i}")

squaredList = []
squaredListOfEvenNumbers = []

for i in aList:
    squaredList.append(i**2)
    if (i % 2 == 0):
        squaredListOfEvenNumbers.append(i**2)


print(f"squaredList = {squaredList}")
print(f"squaredListOfEvenNumbers = {squaredListOfEvenNumbers}")


# Even number: if I devide by two then there should not be any remainder
# MODULO: %
print(f"13 % 2 = {13 % 2}")


### While Loop
i = 1
while i < 2:
    print(f"i = {i}")
    i = i + 1
    print(f"After +1 i = {i}")


cmd = ""
while cmd != "x":
    cmd = input("what's your command: ")
    print(f"cmd = {cmd}")