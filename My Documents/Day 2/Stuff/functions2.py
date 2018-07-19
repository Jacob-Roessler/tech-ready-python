def in_to_cm(In):
    cm = In*2.54
    return cm
In = float(input("Enter an amount of inches: "))
in_to_cm(In)
print(f"{In} inches is {in_to_cm(In)} centimeters")