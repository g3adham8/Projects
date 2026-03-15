import random


def roll():
    result = random.randint(1, 6)
    return result



while True:
    players = input("enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid input! Please enter a number.")

max_score = 50
players_score = [0 for _ in range(players)]

 while max(players_score) < max_score:
    for player_idx in range(players):
        print(f"\n--- Player {player_idx + 1}'s turn ---")
        print(f"Your total score is: {players_score[player_idx]}")

        current_turn_score = 0

        while True:
            user = input("Do you want to roll (y)? ").lower()
            if user != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over, no points added.")
                current_turn_score = 0
                break
            else:
                current_turn_score += value
                print(f"You rolled a: {value}")
                print(f"Current turn score: {current_turn_score}")

        
        players_score[player_idx] += current_turn_score
        print(f"Your total score is now: {players_score[player_idx]}")

        
        if players_score[player_idx] >= max_score:
            break


winning_score = max(players_score)
winning_idx = players_score.index(winning_score)
print(
    f"\nCongratulations! Player {winning_idx + 1} is the winner with a score of: {winning_score}")
