"""   Who's paying?. Banker's Roulette  """
import random, time
seed_number = input("create a seed number: ")
random.seed(seed_number)
print()
names_as_csv = input("Give me everybody's name separated by a comma and space: \n")
names = names_as_csv.split(", ")

content = (len(names)-1)
payer = random.randint(0, content) #randint is inclusive unlike our normal list slicing
print()
num =len(names)*4
for r in range (num):
    if r == round(num/2):
        print('Loading', end='')
    print(' - ', end='')
    time.sleep(0.1)
print()
print()
print(f"{names[payer]} is going to buy the meal today")