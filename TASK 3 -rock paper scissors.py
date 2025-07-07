import random

def get_bot_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    while True:
        choice = input("Enter your move (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

def determine_winner(player, bot):
    if player == bot:
        return "draw"
    elif (player == "rock" and bot == "scissors") or \
         (player == "scissors" and bot == "paper") or \
         (player == "paper" and bot == "rock"):
        return "player"
    else:
        return "bot"

def play_game():
    player_score = 0
    bot_score = 0
    round_number = 1

    print("Welcome to Rock, Paper, Scissors!")
    print("----------------------------------")

    while True:
        print(f"\nRound {round_number}")
        player_choice = get_player_choice()
        bot_choice = get_bot_choice()

        print(f"You chose: {player_choice}")
        print(f"Bot chose: {bot_choice}")

        result = determine_winner(player_choice, bot_choice)

        if result == "draw":
            print("This round is a draw.")
        elif result == "player":
            print("You win this round.")
            player_score += 1
        else:
            print("Bot wins this round.")
            bot_score += 1

        print(f"Current Score - You: {player_score} | Bot: {bot_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing!")
            print(f"Final Score - You: {player_score} | Bot: {bot_score}")
            break

        round_number += 1

# Start the game
play_game()
