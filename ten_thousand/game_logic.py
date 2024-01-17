import random
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate and return the score for a given dice roll.

        Parameters:
        dice_roll (tuple of int): A tuple representing the dice roll.

        Returns:
        int: The calculated score.
        """
        score = 0
        rolls = Counter(dice_roll)

        if set(dice_roll) == set(range(1, 7)):
            return 1500

        # Three Pair
        if len(rolls) == 3 and all(roll == 2 for roll in rolls.values()):
            return 1500

        for num, roll in rolls.items():
            if roll >= 3:
                if num == 1:
                    score += 1000 * (roll - 2)  # N of a kind 1
                else:
                    score += num * 100 * (roll - 2)  # N of a kind others

        # Leftover 1s and 5s
        if rolls[1] < 3:
            score += rolls[1] * 100
        if rolls[5] < 3:
            score += rolls[5] * 50

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice and return the results.

        Parameters:
        num_dice (int): The number of dice to roll.

        Returns:
        tuple: A tuple containing the results of each dice roll.
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def set_aside_dice(dice_roll, dice_to_set_aside):
        """
        Set aside specific dice from the current roll.

        Parameters:
        dice_roll (tuple of int): Current dice roll.
        dice_to_set_aside (tuple of int): Dice to set aside.

        Returns:
        tuple of int: Remaining dice after setting aside.
        """
        remaining_dice = tuple(dice for dice in dice_roll if dice not in dice_to_set_aside)
        return remaining_dice


class Game:
    def play_game(self):
        total_score = 0
        current_round = 1
        max_rounds = 10  # You can adjust the maximum number of rounds as needed

        while current_round <= max_rounds:
            # Roll the dice
            dice_roll = GameLogic.roll_dice(6)

            print(f"\n--- Round {current_round} ---")
            print(f"Current dice roll: {dice_roll}")

            # Allow the user to set aside dice
            set_aside = self.get_user_input_for_set_aside(dice_roll)

            # Calculate the score for the remaining dice
            remaining_dice = GameLogic.set_aside_dice(dice_roll, set_aside)
            score = GameLogic.calculate_score(remaining_dice)

            print(f"Score for this round: {score}")

            # Allow the user to bank or roll again
            user_decision = self.get_user_decision()

            if user_decision == "bank":
                total_score += score
                print(f"Current Round: {current_round}, Total Score: {total_score}")
                current_round += 1
            else:
                print("Rolling again...")

        print("Game Over!")

    def get_user_input_for_set_aside(self, dice_roll):
        print("Do you want to set aside any dice? (y/n)")
        user_input = input().lower()

        if user_input == 'y':
            print("Enter the dice numbers to set aside (e.g., 1 3 5):")
            set_aside_input = input().split()
            set_aside_dice = tuple(int(dice) for dice in set_aside_input)
            return set_aside_dice
        else:
            return tuple()

    def get_user_decision(self):
        print("Do you want to bank your current score or roll again? (bank/roll)")
        user_decision = input().lower()

        while user_decision not in ['bank', 'roll']:
            print("Invalid choice. Please enter 'bank' or 'roll'.")
            user_decision = input().lower()

        return user_decision


# Example usage:
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
