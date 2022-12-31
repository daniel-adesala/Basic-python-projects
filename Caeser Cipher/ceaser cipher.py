import ceaser_cipher_art

def caesar(plain_text, shift_amount, direction):
  caeser_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift_amount
      elif direction == "decode":
        new_position = (position + 26) - shift_amount
      new_letter = alphabet[new_position]
      caeser_text += new_letter
    else:
      caeser_text += letter
  print(f"The {direction}d text is {caeser_text}")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(ceaser_cipher_art.logo)
continue_ = 'yes'
while continue_ == 'yes':
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25:
    shift %= 25
  caesar(plain_text = text, shift_amount = shift, direction = direction)
  continue_ = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
print("Goodbye")
