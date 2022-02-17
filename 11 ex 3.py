import math

def circle_calc(radius):
    area = round(math.pi*(radius*radius),2)
    circum = round(2*math.pi*radius,2)
    dia = round(2*radius,2)
    return area,circum, dia


if __name__ == '__main__':
    r = input("Enter a radius: ")
    r = float(r)
    area, c, d = circle_calc(r)
    print(f"area: {area}, circumference: {c}, Diameter: {d}")
