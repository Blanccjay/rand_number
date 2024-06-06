# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:31:54 2024

@author: thant
"""
import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You are correct!")
        break
    elif user_guess > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You guessed the answer in", guesses, "guesses!!")