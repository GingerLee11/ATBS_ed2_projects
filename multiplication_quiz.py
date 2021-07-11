# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 14:53:58 2021

@author: Cleme
"""

#! python3
# Multi_quiz.py - Multiplication Quiz that prompts users with
# 10 mutliplication questions from 0 x 0 to 9 x 9

from random import randint
import time

def multi_quiz():
    print('Ten Question Multiplication Quiz.')
    print('You have 3 attempts per question.')
    print('There is an 8 second time limit per question.')
    print('Good Luck!\n')
    time.sleep(2)
    
    # User prompt
    user_prompt = 'Please input an integer.'
    
    # Time limit constant and time between questions constant
    sleep_secs = 1
    time_limit = 8
    
    # Set correct answers to zero
    correct_ans = 0
    # For loop to loop through ten multiplication questions
    for question in range(10):
        time_initial = time.time()
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        ans = num1 * num2 
        for attempt in range(3):
            print(f"Question {question+1}: (Attempt {attempt+1})")
            print(f"{num1} x {num2} =")
            user_ans = input()
            time_final = time.time()
            try:
                if int(user_ans) == ans:
                    if time_final - time_initial > time_limit:
                        print("More than 8 seconds have passed.")
                        time.sleep(sleep_secs)
                        break
                    elif time_final - time_initial < 8:   
                        print('Correct!')
                        correct_ans += 1
                        time.sleep(sleep_secs)
                        break
                elif int(user_ans) != ans:
                    print('Incorrect. Please try again.')
                    time.sleep(sleep_secs)
            except: 
                print(user_prompt)
                time.sleep(sleep_secs)
            
    print(f'You got {correct_ans} answers correct out of 10!')           

multi_quiz()
