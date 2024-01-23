print("BMI Calculator")
print(" ------------ ")

# Input weight in kilograms and height in centimeters from the user
weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

# Convert height from centimeters to meters
height_m = height_cm / 100  # Convert cm to meters

# Calculate BMI
bmi = weight / (height_m ** 2)

# Display BMI
print("Your BMI is:", bmi)

# Interpret BMI
if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi < 25:
    print("You are Normal weight")
elif 25 <= bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
