from ten_thousand.game_logic import GameLogic 

def play(roller=None):
    """
Initiates the Ten Thousand game.

Parameters:
- roller (function): Dice-rolling function; defaults to GameLogic.roll_dice if not provided.

Returns:
Shows the welcome message and prompts the user to begin the game, then calls start_game with the specified dice roller.
"""

    if roller is None:
        roller = GameLogic.roll_dice
    welcome()
    response = input("> ")
    if response.lower() == "n":
        print("Certainly, whenever you're ready")
    else:
        start_game(roller)

def welcome():
    print("Greeting for the Ten Thousand game.")
    print("Options: (y)es to start, (n)o to skip.")

def roll_dice(roller, dice_remaining):
    print(f"Rolling dice...")
    return roller(dice_remaining)

def get_dice_to_bank(dice_rolled):
    while True:
        dice_str = " ".join(map(str, dice_rolled))
        print(f"*** {dice_str} ***")
        print("Enter dice to keep, or (q)uit:")
        keep_response = input("> ").strip()

        if keep_response.lower() == "q":
            return None

        try:
            dice_kept = tuple(int(die) for die in keep_response)
            if not all(die in dice_rolled for die in dice_kept):
                print("Invalid input. Please enter only the dice that were rolled.")
                continue
            return dice_kept
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def handle_player_action():
    print("(r)oll again, (b)ank your points, or (q)uit:")
    return input("> ").lower()

def bank_points(total_score, score, round):
    total_score += score
    print(f"You banked {score} points in round {round}")
    print(f"Total score is {total_score} points")
    return total_score

def start_game(roller):
    total_score = 0
    round = 1
    dice_remaining = 6

    while True:
        print(f"Starting round {round}")
        dice_rolled = roll_dice(roller, dice_remaining)

        dice_kept = get_dice_to_bank(dice_rolled)
        if dice_kept is None:
            print(f"Thanks for playing. You earned {total_score} points")
            break

        score = GameLogic.calculate_score(dice_kept)
        dice_remaining -= len(dice_kept)
        print(f"You have {score} unbanked points and {dice_remaining} dice remaining")

        action = handle_player_action()

        if action == "b":
            total_score = bank_points(total_score, score, round)
            round += 1
            dice_remaining = 6
        elif action == "r":
            if dice_remaining == 0:
                dice_remaining = 6
        elif action == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break

if __name__ == "__main__":
    play()
