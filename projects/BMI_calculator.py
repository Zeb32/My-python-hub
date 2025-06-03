name = input("Enter your name: ")
weight = input("Enter your weight in Pounds: ")
height = input("Enter your height in Inches: ")

BMI = (int(weight) / (int(height) * int(height))) * 703

print("Your BMI is: " + str(round(BMI, 2)))

if BMI > 0:
    if BMI < 18.5:
        print("Mr." + name + ", You are underweight.")
    elif BMI >= 18.5 and BMI < 24.9:
        print("Mr." + name + ", You are normal weight.")
    elif BMI >= 25 and BMI < 29.9:
        print("Mr." + name + ", You are overweight.")
    elif BMI >= 30:
        print("Mr." + name + ", You are obese.")
    else:
        print("Invalid BMI value.")
