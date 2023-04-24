# The hangman game is a word guessing game where the player
# is given a word and has to guess the letters that make up the word.

# The player is given a certain number of tries (no more than
# 6 wrong guesses are allowed) to guess the correct letters
# before the game is over.

secret_word = "Java"                        # the secret word
used_letters = []                           # the used letters
guessed_letters = ["_"] * len(secret_word)  # the guessed letters of the secret word
tries = 6                                   # the maximum number of wrong tries

while tries > 0:

    # print game info
    print(f"\nYou have {tries} tries left.")
    print("Used letters: ", ", ".join(used_letters))
    print("Word: ", " ".join(guessed_letters))

    # input a letter and check if only one letter was entered
    letter = input("\nGuess a letter: ")
    if len(letter) != 1:
        print("Only one letter is allowed!")
        continue

    # check if the letter has already been tried
    if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
        print("This letter has already been tried!")
        continue

    # check if the guess was wrong
    used_letters.append(letter)
    if letter not in secret_word:
        tries -= 1

    # determine the guessed letters of the secret word
    for i in range(len(secret_word)):
        char = secret_word[i]
        if char.lower() in used_letters or char.upper() in used_letters:
            guessed_letters[i] = char

    # the winning condition of the game
    win = secret_word == "".join(guessed_letters)
    if win: break

# final check
if win:
    print(f"\nYou guessed the word \"{secret_word}\"!")
else:
    print(f"\nYou failed to guess the word \"{secret_word}\"!")
