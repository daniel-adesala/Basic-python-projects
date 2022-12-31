
print ("""
 Hello, Welcome.
 Let's calculate
 """)
restart = ""
while True:
  if restart != "": 
    break
  else:
    calculate = input ("What do you want me to calculate? : ")
    calculate_ = calculate.replace('^', '**')
    print ("Answer: ",eval(calculate_))
    restart = input ("Tap ENTER to perform another operation, or Insert any character to end: ")
