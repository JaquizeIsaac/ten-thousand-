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
