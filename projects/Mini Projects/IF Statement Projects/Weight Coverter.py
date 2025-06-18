# Python Weight Converter # This program converts weight from pounds to kilograms and vice versa

Weight = float(input("Enter your weight: "))
unit = input("Enter your unit (pounds - L or kilograms -k): ")

if unit.lower() == 'k':
    Weight = Weight * 2.20462
    unit = 'Lbs'
    print(f"Your weight in pounds is: {round(Weight, 2)} {unit}")
elif unit.lower() == 'l':
    Weight = Weight / 2.20462
    unit = 'Kg'
    print(f"Your weight in kilograms is: {round(Weight, 2)} {unit}")
else:
    print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")