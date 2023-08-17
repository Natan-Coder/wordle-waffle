# Process guess function
def inputguess(secret_word, guess):
    position = 0
    clue = ""
    for letter in guess:
        if letter == secret_word[position]:
            clue += "Y"
        elif letter in secret_word:
            clue += "X"
        else:
            clue += "N"
        position += 1
    print(clue)
    return clue == "YYY"  # True if correct, False otherwise


# Checkword guess function
def checkword(word):
    if (len(word) != 5) or word.isalpha() == False:
        return False
    else:
        return True


game_over_attempts = 6
total_attempts = 0
correct_answer = False
wrong_answer = True

while total_attempts < 6 and not correct_answer:
    secret_word = "bored"
    # Get guess from user
    guess = input("Input a 5-letter word and press enter: ")
    print("You have guessed", guess, "you have", game_over_attempts - total_attempts, "guesses remaining.")
    total_attempts += 1

    # Process guess
    correct_answer = inputguess(secret_word, guess)

    # Checkword guess - Loop Into ProcessGuess

    while checkword(guess) == False and total_attempts <= 6 and not correct_answer:
        print("Invalid word, please only letters and 5 letters long...")
        break

    if checkword(guess) == True and total_attempts <= 8 and not correct_answer:
        print("Incorrect!")

    else:
        inputguess

# Endgame message
if correct_answer:
    print("Congrats kid, you guessed the word in:", total_attempts, "times.")

elif wrong_answer:
    print("You tried my guy, the correct word is '", secret_word, "'.")