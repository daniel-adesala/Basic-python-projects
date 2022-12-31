import random, hangman_art, hangman_words
# asking user for input and checking user's answers
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)


display = []

for blanks in range(0, len(chosen_word)):
    display.append("_")

lives = 6

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've guessed the letter {guess} already,guess again")
        continue
    for position in range(0, len(chosen_word)):
        r = chosen_word[position]
        if r == guess:
            display[position] = r
    
    if guess not in chosen_word:
        print(
            f"You guessed the letter {guess}, that's not in the word, you lose a life."
        )
        lives -= 1

    if lives == 0:
        print("Game Over")
        break
    print(hangman_art.stages[lives])
    print(display)
if "_" not in display:
    print("You win")