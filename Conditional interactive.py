#Make an interactive questionnaire using formatted strings.
#Return the total result of the questionnaire in an interactive way.
###########################

print ("Hello, Good day")
print()
bot_name = 'If_Else Stark'
#1
name = input(f"My name is {bot_name}, what's your name?:  ")
print()
#2

while True:
    age = input( f"Such lovely name you've got there {name}. How old are you?: ")
    if age.isdigit() and 0 < int(age) < 1000: break
    else: print ("insert only numbers")
print()

#3
sex = input (f"{name}, what is your sexual orientation?; ")
print ()
#4
country = input (f"Which contry do you live in, {name}?:  ")
print()

colours = ['red', 'green', 'blue', 'yellow', 'white', 'black' ]
print (colours)
print()
#5
color = input ("from the colours listed above, which is your preferred colour: ").lower()
while color not in colours:
    print (f"{color} isn't part of the colours listed above")
    color = input ("from the colours listed above, which is your preferred colour: ").lower()
print()
if color in colours:
   print (f" {color} is such a beautiful colour, nice preference {name} ")    
print()
if color == colours[0]:
    print (f"{color} signifies Love, represents Life.")
elif color == colours[1]:
    print (f"{color}  signifies nature, represents growth and renewal.")
elif color == colours[2]:
    print (f"{color}  signifies freedom , represents the sky and sea.")
elif color == colours[3]:
    print (f"{color}  signifies happiness, represents enlightenment and creativity.")
elif color == colours[4]:
    print (f"{color}  signifies peace, represents purity or innocence.")
elif color == colours[5]:
    print (f"{color}  signifies Power, represents elegance and sophistication.")
print()
#6
pos = input("Are you a student? (answer yes or no):  ").lower()
if pos == "yes":
    school = input ("What School do you study?: ")
    course = input ("What course are you studying?: ")
    print()
    print (f"wow, studying {course}, in {school} is such a flex, i'm impressed")
else:
    occupation = input("What's your occupation? : ")
print()   
print (f"That's all for now {name}, it's been nice discussing with you ")
print()
print (f"Goodbye, {name}")
print()

input ("press ENTER to continue:")

print ("*" * 30)

print()
# Total output
print (f"I am {bot_name}, I just had a conversation with {name}")
print()
print (f"""{name}, is {age} years old, a {sex}, 
{name} lives in {country}, and likes colour {color}""")
if pos == "yes":
    print (f"{name} is studying {course} in {school}. ")
else:
    print (f"{name} is a {occupation}.")
print()
print (f"Once again i am {bot_name} ")
print ("Goodbye")






    


