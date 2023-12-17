word = "Eldridge"
guess = ''
tries = 0


while guess != word and not (tries > 2):
    if tries > 2:
        print("You lost")
    else:
        guess = input("What is the secret word: ")
        tries += 1
        if guess == word:
            break


print(tries)

