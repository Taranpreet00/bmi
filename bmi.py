""" This is a BMI calculator 
"""
print("This is a BMI calculator")
name=str(input("Enter your name "))
mass=int(input("Enter your weight in kg's"))
height=float(input("Enter your height in meters"))
#maths start here
bmi=mass/(height*height)
print(f'Hey {name}, your height is {height}, your weight is {mass} and your BMI is {bmi} ')