print("Welcome to Love calculator!")
Name1 = input("What is your name? \n").lower()
print()
Name2 = input("What is your name? \n").lower()
print()
t = Name1.count("t") + Name2.count("t")
r = Name1.count("r") + Name2.count("r")
u = Name1.count("u") + Name2.count("u")
e = Name1.count("e") + Name2.count("e")

l = Name1.count("l") + Name2.count("l")
o = Name1.count("o") + Name2.count("o")
v = Name1.count("v") + Name2.count("v")
e = Name1.count("e") + Name2.count("e")

true = (t + r + u + e)
love = (l + o + v + e)
love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score >= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
