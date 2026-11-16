def name_of_function():
    pass

def calculate_velocity(distance, time):
    v = distance/time
    print("The velocity with distance", distance, "and time", time, "=", v)

def area_of_circle(radius):
    area = 3.142*radius*radius
    print("The area of the circle with radius", radius, "=", area)

choice = input("What do you want to calculate? \n1. Velocity\n2. Area of a circle\n3. Exit ")

while True: 
    if choice == "1":
        distance = float(input("Enter the distance: "))
        time = int(input("Enter the time: "))
        calculate_velocity(distance, time)
 
    elif choice == "2":
        radius = int(input("Enter the radius: "))
        area_of_circle(radius)

    elif choice == "3":
        print("Later!")
        break

    else:
        print("Invalid input.")