###BMI calculator 
print("Welcome to BMI calculator 2.0")
print()
weight = float(input("Insert your weight in kg: "))
print()
height = float(input("Insert your height in m: "))
print()
bmi = round(weight / (height**2), 1)
print()
print(f"Your BMI value is: {bmi}")
print()
if bmi < 18.5:
  print ("You are UNDERWEIGHT")
elif bmi > 18.5 and bmi < 25:
  print("You have a NORMAL WEIGHT")
elif bmi > 25 and bmi< 30:
  print ("You are OVERWEIGHT")
elif bmi > 30 and bmi < 35:
  print ("You are OBESE")
elif bmi > 35:
  print ("You are clinically OBESE")









