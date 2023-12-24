import random


def die():
    roll = random.randint(1, 6)
    return roll


while True:
    try:
        players = int(input("Enter the number of players: "))

        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")

    except ValueError:
        print("Invalid input, try again")


max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)


while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number", player_idx+1, "turn has just started\n")
        current_score = 0

        while True:

            should_roll = input("Do you want to roll (y): ")
            if should_roll.lower() != "y":
                break
            value = die()
            if value == 1:
                current_score = 0
                print("You rolled a 1. Turn done!")
                break
            else:
                current_score += value
                print("You rolled a {}".format(value))

            print("Your score is {}".format(current_score))

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print("Player number", winning_idx + 1, "is the winner with a score of", max_score)













