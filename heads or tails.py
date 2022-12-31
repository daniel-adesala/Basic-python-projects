####Heads or Tails
import random
from random import randint

print("Welcome to Heads or Tails")
seed_number = input("Insert any  number: ")
random.seed(seed_number)

result = randint(0, 1)
if result == 0:
    print("Heads")
else:
    print("Tails")
    