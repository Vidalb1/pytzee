"""
File:    pytzee.py
Author:  Vidal Bickersteth
Date:    11/01/2024
Section: 16-DIS(1383)
E-mail:  vidalb1@umbc.edu
Description: This program computes the real pytzee game in a single-player version.
"""

import random

TOTAL_DICE = 5
DICE_FACES = 6



def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list



def play_game(num_rounds):
        """    A function to play the pytzee game.
            :param num_rounds: The number of rounds the user wants to play.
        """
        final_score = 0
        scores_1 = 0
        counter = 0
        dice = roll_dice()
        lists = []
        modes = {"Three of a Kind": 0,"Four of a Kind": 0, "Full House": 0, "Small Straight": 0,"Large Straight": 0,"Pytzee": 0, "Chance": 0}
        user = {"1's": 0,    "2's": 0,    "3's": 0,    "4's": 0,   "5's": 0,   "6's": 0}
        for i in range(1, num_rounds + 1):
            print(f"***** Beginning Round {i} *****")
            print(f"    Your score is: {scores_1}")
            print(" ".join(str(dice)))
            users = input("How would you like to count this dice roll? ")
            inputs = lower_function(users)
            if("count" in inputs):
                split = inputs.split(" ")
                if("s" in user):
                    print("Please don't include s' in your input. Try again!")
                    users = input("How would you like to count this dice roll? ")
                    inputs = lower_function(users)    
                elif(split[1] in lists):
                    print("There was already a score in that slot.")
                    users = input("How would you like to count this dice roll? ")
                    inputs = lower_function(users)
            elif(inputs in lists):
                print("There was already a score in that slot.")
                users = input("How would you like to count this dice roll? ")
                inputs = lower_function(users)
            if(inputs != "skip"):
                if("count" in inputs):
                    score1 = 0
                    split = inputs.split(" ")
                    print("Accepted the", split[1])
                    score1 += get_number(dice,inputs)
                    lists.append(split[1])
                    for keys in user.keys():
                        if(split[1] in keys):
                            user[keys] = score1
                    scores_1 += score1
                    lists.append(inputs)
                elif(inputs == "three of a kind" or inputs == "four of a kind" or inputs == "3 of a kind" or inputs == "4 of a kind"):
                    score2 = 0    
                    if(detect_kind(dice) > 0):
                        print("Three of a Kind!")
                        score2 += detect_kind(dice)
                        for keys in modes.keys():
                            if(users == keys.lower()):
                                modes[keys] = score2
                    scores_1 += score2
                    lists.append(inputs)
                elif(inputs == "full house"):
                    score3 = 0
                    score3 += full_house(dice)
                    if(full_house(dice) > 0):
                        print("You have a full house and will be awarded 25 points.")
                    for keys in modes.keys():
                        if (users == keys.lower()):
                            modes[keys] = score3
                    scores_1 += score3
                    lists.append(inputs)
                elif(inputs == "small straight"):
                    score4 = 0
                    score4 += small_straight(dice)
                    for keys in modes.keys():
                        if(users == keys.lower()):
                            modes[keys] = score4
                    if(small_straight(dice) > 0):
                        print("You have a small straight and get 30 points.")
                    scores_1 += score4
                    lists.append(inputs)
                elif(inputs == "large straight"):
                    score5 = 0
                    score5 += large_straight(dice)
                    for keys in modes.keys():
                        if(users == keys.lower()):
                            modes[keys] = score5
                    if(large_straight(dice) > 0):
                        print("You have a large straight and get 40 points.")
                    scores_1 += score5
                    lists.append(inputs)
                elif(inputs == "pytzee"):
                    score6 = 0
                    if(counter > 0 and pytzee(dice) > 0):
                        print("You have an extra pytzee and get 100 points.")
                        score6 += 100
                    elif(pytzee(dice) > 0):
                        print("You have a pytzee and get 50 points.")
                        score6 += pytzee(dice)
                    for keys in modes.keys():
                        if(users == keys.lower()):
                            modes[keys] += score6
                    scores_1 += score6
                    counter += 1
                elif(inputs == "chance"):
                    score7 = 0
                    if(chance(dice) > 0):
                        print("You have a chance box!")
                        score7 += chance(dice)
                    for keys in modes.keys():
                        if(users == keys.lower()):
                            modes[keys] = score7
                    scores_1 += score7
                    lists.append(inputs)
            dice = roll_dice()
            print(" ")
            print("   	  Scorecard:")
            print(f"     {user}")
            print(f"     {modes}")
        for values2 in user.values():
            final_score += values2
        scores_1 += score_2(final_score)
        print(" ")
        print("Your final score was", scores_1)


def get_number(rolled_list, user_count):
    """    A function to count all the number of dice with the number the user have.
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :param user_count: The user input of the number they want to count.
            :return: The sum of number's the user have. 
    """
    points = 0
    split = user_count.split(" ")
    for i in range(len(rolled_list)):
        if(int(split[1]) == rolled_list[i]):
            points += rolled_list[i]
    return points


def detect_kind(rolled_list):
    """    A function to detect three or four of a kind on the rolled list
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: the sum of the whole rolled_list if there's three or four of a kind in the rolled list.
    """
    sum = 0
    counter = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    for i in range(len(rolled_list)):
        if(rolled_list[0] == rolled_list[i]):
            counter += 1
        elif(rolled_list[1] == rolled_list[i]):
            counter2 += 1
        elif(rolled_list[2] == rolled_list[i]):
            counter3 += 1
        elif(rolled_list[3] == rolled_list[i]):
            counter4 += 1
        elif(rolled_list[4] == rolled_list[i]):
            counter5 += 1
    if(counter == 3 or counter == 4 or counter2 == 3 or counter2 == 4 or counter3 == 3 or counter3 == 4 or counter4 == 3 or counter4 == 4 or counter5 == 3 or counter5 == 4):
        for i in range(len(rolled_list)):
            sum += rolled_list[i]
    return sum

def full_house(rolled_list):
    """    A function to detect if there's a full house in the rolled dice.
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: An awarded 25 points if the rolled list have a three of a kind and a different pair of another type.
    """
    points = 0
    counter = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    for i in range(len(rolled_list)):
        if(rolled_list[0] == rolled_list[i]):
            counter += 1
        elif(rolled_list[1] == rolled_list[i]):
            counter2 += 1
        elif(rolled_list[2] == rolled_list[i]):
            counter3 += 1
        elif(rolled_list[3] == rolled_list[i]):
            counter4 += 1
        elif(rolled_list[4] == rolled_list[i]):
            counter5 += 1
    if(counter == 3 or counter2 == 3 or counter3 == 3 or counter4 == 3 or counter5 == 3):
        if(counter == 2 or counter2 == 2 or counter3 == 2 or counter4 == 2 or counter5 == 2):
            points += 25
    return points

def small_straight(rolled_list):
    """    A function to detect if there's a small straight in the rolled list.
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: An awarded 30 points if there is a 4 in sequence of the rolled list.
    """
    points = 0
    counter = 1
    number = 0
    rolled_list.sort()
    for i in range(len(rolled_list) - 1):
        number = rolled_list[i]
        sum = (number) + 1
        if(sum == rolled_list[i+1] ):
            counter += 1
    if(counter == 4):
        points += 30
    return points
            


def large_straight(rolled_list):
    """    A function to detect if there's a large straight in the rolled list.
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: An awarded 40 points if there is a 5 in sequence of the rolled list.
    """
    points = 0
    counter = 1
    number = 0
    rolled_list.sort()
    for i in range(len(rolled_list) - 1):
        number = rolled_list[i]
        sum = (number) + 1
        if(sum == rolled_list[i+1]):
            counter += 1
    if(counter == 5):
        points += 40
    return points

def pytzee(rolled_list):
    """    A function to check if there's a pytzee in the rolled_list
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: Awarded 50 points if all of the five dice are the same.
    """
    points = 0 
    counter = 1
    for i in range(len(rolled_list) - 1):
        if(rolled_list[i] == rolled_list[i+1]):
            counter += 1
    if(counter == len(rolled_list)):
        points += 50
    return points


def chance(rolled_list):
    """    A function to calculate the sum of the rolled list into the chance box.
            :param rolled_list: A list of 5 dice rolls between the numbers 1 through 6.
            :return: the sum of the rolled list.
    """
    chance_box = 0
    for i in range(len(rolled_list)):
        chance_box += rolled_list[i]
    return chance_box


def score_2(user_score):
    """    A function to calculate if the user's score is 63 or higher, then an additional 35 points will be awarded.
            :param user_score: The user's score of all the 1s,2s,3s,4s,5s,and 6s.
            :return: the sum of the rolled list.
    """
    user = user_score
    if(user >= 63):
        user = 35
        return user
    return 0
    

def lower_function(user_input):
    """    A function to lowercase the user input.
            :param user_input: the user's input.
            :return: the lowercased user's input.
    """
    user = user_input.lower()
    return user


if __name__ == '__main__':
    # Generates the number of rounds and seeds that the user wants to select
    #   in order to play the pytzee game.
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)



