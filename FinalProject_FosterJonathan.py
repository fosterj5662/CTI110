# Jonathan Foster
# 5/12/26
# Final Project
# This project is a guessing game

import random
import time

def create_character():
    return {
        "name": "Sunny",
        "hearts": 3,
        "points": 0,
        "clues": 0,
        "toy": "candy"
    }

def show_status(player):
    print(f"\n{player['name']} ❤️ Hearts: {player['hearts']} | ⭐ Points: {player['points']} | 🔎 Clues: {player['clues']}")

def get_guess():
    while True:
        guess = input("Guess the secret number (1-3): ")
        if guess in ["1", "2", "3"]:
            return int(guess)
        print("Please type 1, 2, or 3.")

def play_round(player):
    secret = random.randint(1, 3)
    print("\nSunny is hiding behind one door...")
    time.sleep(1)

    guess = get_guess()

    if guess == secret:
        print("Yay! You found Sunny! 🎉")
        player["points"] += 1
        player["clues"] += 1
        player["toy"] = "star"
        return True
    else:
        print(f"Oh no! Sunny was behind door {secret}. Try again!")
        player["hearts"] -= 1
        player["toy"] = "cloud"
        return False

def game_over(player):
    print("\nGame over!")
    print(f"{player['name']} got {player['points']} points and {player['clues']} clues.")

    if player["points"] >= 3:
        print("Great job! You are a guessing star! 🌟")
    else:
        print("Good try! Play again and find more Sunny surprises!")

def main():
    print("Welcome to Sunny Guess! 🌈")
    print("Help Sunny hide and seek!")

    player = create_character()

    while player["hearts"] > 0 and player["points"] < 3:
        show_status(player)
        play_round(player)
        time.sleep(0.8)

    game_over(player)

if __name__ == "__main__":
    main()






'''In Python; make me a guessing game a 5 year old can play with these parameters: The game MUST use functions (including a main function to run the program)
The game should include at least one main character/object that is represented by a Python dictionary.
You can choose to include an inventory for your character which will most likely be another dictionary. The game must import and use the random and time Python libraries .The game may include emojis to make it more visually appealing
During game play, the main character’s key:value pairs should change as the game is played'''
