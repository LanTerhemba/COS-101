def velocity(distance, time):
        print("Velocity =", v, "m/s")

def acceleration(final_velocity, initial_velocity, time):
        print("Acceleration =", a, "m/s²")

def force(mass, acceleration_value):
    print("Force =", f, "N")

def kinetic_energy(mass, velocity_value):
    print("Kinetic Energy =", ke, "J")

def momentum(mass, velocity_value):
    print("Momentum =", p, "kg m/s")

while True:
    
    print("What do you want to calculate?")
    print("1. Velocity")
    print("2. Acceleration")
    print("3. Force")
    print("4. Kinetic Energy")
    print("5. Momentum")
    print("6. Exit")
    
    calculation = input("Select a formula (1-5) or enter 6 to exit: ")
    
    
    if calculation == "1":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
    
        if time == 0:
            print("Time can't be zero.")
        else:
            v = distance / time
        velocity(distance, time)
    
    elif calculation == "2":
        final_velocity = float(input("Enter final velocity: "))
        initial_velocity = float(input("Enter initial velocity: "))
        time = float(input("Enter time: "))
    
        if time == 0:
            print("Time can't' be zero.")
        else:
            a = (final_velocity - initial_velocity) / time
        acceleration(final_velocity, initial_velocity, time)
    
    elif calculation == "3":
        mass = float(input("Enter mass: "))
        acceleration_value = float(input("Enter acceleration: "))
    
        f = mass * acceleration_value
        force(mass, acceleration_value)
    
    elif calculation == "4":
        mass = float(input("Enter mass: "))
        velocity_value = float(input("Enter velocity: "))
    
        ke = 0.5 * mass * velocity_value ** 2
        kinetic_energy(mass, velocity_value)
    
    elif calculation == "5": 
        mass = float(input("Enter mass: "))
        velocity_value = float(input("Enter velocity: "))
    
        p = mass * velocity_value
        momentum(mass, velocity_value)
    
    elif calculation == "6":
        print("Later now my guy")
        break
        
    else:
        print("Invalid request, pick a number from 1 to 6")
