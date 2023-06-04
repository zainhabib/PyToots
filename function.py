def calcCircleArea(radius) :
    pi = 3.14
    return pi * radius ** 2

def myFunc1() :
    print("in myFunc1")

def myMainFunc() :
    myFunc1()
    print("In myMainFunc")


myMainFunc()

areaOfCircle1 = calcCircleArea(3.4)
print(f"areaOfCircle1 = {areaOfCircle1}")

areaOfCircle2 = calcCircleArea(3)
print(f"areaOfCircle2 = {areaOfCircle2}")

val = "3.4"
val = float(val)