age = 19
height = 190.0
comp = 4+3j

def area():
    base = eval(input("Enter base: "))
    height = eval(input("Enter height: "))

    while True:
        tri = 0.5 * base * height
        print('The area of the triangle is ' , tri )
        break
area()

def perimeter():
    a = eval(input("Enter side a: "))
    b = eval(input("Enter side b: "))
    c = eval(input("Enter side c: "))

    while True:
        peri = a + b + c
        print('The perimeter of triangle is ' , peri)
        break
perimeter()

def area_rectangle():
    pass