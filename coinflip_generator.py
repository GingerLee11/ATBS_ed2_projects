# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 07:35:28 2021

@author: Cleme
"""
#! python3 
# coinflip_generator.py - Generated X coin flips X times and counts the number of times 
# heads or tails comes up X times in a row


# import the random module and set the number of streaks to 0 before the loop
import random


# defines the function coinflip_generator which takes in the number of experiments to run
# the number of coinflips per experiment and the streak threshold to add a streak
def coinflip_generator(experiments, coinflips, streaks):
    # Set the number of experiments and the number of coinflip per experiment
    num_of_experiments = experiments
    num_of_coinflips = coinflips
    # Number of streak of heads or tails in a row to calc prob for
    streak_num = streaks
    # Initialize the number of streaks to zero
    number_of_streaks = 0 
    # create the empty list of lists
    total_h_and_t = []
    for exp_num in range(num_of_experiments):
        # Create the empty list that the heads and tails will go into
        h_and_t = []
        for coin_flip in range(num_of_coinflips):
            # Generates 1 and 0 randomly to simulate a coin toss
            flippy = random.randint(0, 1)
            # If the 1, heads is appended to the list and if 0, tails is appended. 
            if flippy == 1:
                h_and_t.append('H')
            elif flippy == 0:
                h_and_t.append('T')
        total_h_and_t.append(h_and_t)
     
    for h_and_t in total_h_and_t:
        h_count = 0 
        t_count = 0
        for coin_flip in h_and_t:
            # Counters for heads and tails
            # When head comes up 1 is added to the heads count and the tails count
            # is set back to zero and vice versa
            if coin_flip == 'H':
                h_count += 1
                t_count = 0
                # If the heads count reaches a certain number then a streak is added
                if h_count == streak_num:
                    number_of_streaks += 1
                    h_count = 0 
            elif coin_flip == 'T':
                t_count += 1
                h_count = 0
                # If the tails count reaches a certain number then a streak is added
                if t_count == streak_num:
                    number_of_streaks += 1
                    t_count = 0 
        # If the count reach the streak number, then a streak is added and the count is reset to 0
    return print(number_of_streaks)

coinflip_generator(10000, 100, 20)
               

# TODO: loop through the coinflip generator several times to take the average of the numbers that are generated