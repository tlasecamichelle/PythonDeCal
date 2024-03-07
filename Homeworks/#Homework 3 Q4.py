#Homework 3 Q4

height = float(input("input your height in meters: "))

weight = float(input("input your weight in kilograms: "))

bmi = weight / (height * height)
rounded_bmi = round(bmi, 2)

print("your bmi is: ", rounded_bmi)