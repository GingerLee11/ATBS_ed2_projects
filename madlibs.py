# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 07:41:35 2021

@author: Cleme
"""

#! python3
# madlibs.py - Mad Libs program that reads in text files and lets users 
# add text anywhere the words ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import os
from pathlib import Path
import re

text = 'The ADJECTIVE ANIMAL VERB into the ADJECTIVE bar, and VERB a(n) NOUN.'

os.chdir(r'C:\Users\Cleme\Practice_Code\Automate_The_Boring_Stuff\ATBS_side_projects')

with open('madlibs.txt', 'r') as madlibs: 
    read_madlibs = madlibs.read()

def madlib_generator(text_file):
    # define parts of speech
    parts_of_speech = [
     'ADJECTIVE',
     'NOUN',
     'ADVERB',
     'VERB',
     'ANIMAL',
     'EXCLAMATION',
    ]
    #match adjectives                           
    adj_regex = re.compile(r'(ADJECTIVE)')
    adj_matches = adj_regex.findall(text_file)
    # match nouns
    noun_regex = re.compile(r'(NOUN)')
    noun_matches = noun_regex.findall(text_file)
    # match adverb
    adverb_regex = re.compile(r'(ADVERB)')
    adverb_matches = adverb_regex.findall(text_file)
    # match verb
    verb_regex = re.compile(r'(VERB)')
    verb_matches = verb_regex.findall(text_file)
    # match animal
    animal_regex = re.compile(r'(ANIMAL)')
    animal_matches = animal_regex.findall(text_file)
    # match exclamation
    exclamation_regex = re.compile(r'(EXCLAMATION)')
    exclamation_matches = exclamation_regex.findall(text_file)
    
    # TODO: create a list of lists to loop through for the sub expressions
    match_list = [
                adj_matches,
                noun_matches,
                adverb_matches,
                verb_matches,
                animal_matches,
                exclamation_matches
                 ]
    madlib_dict = dict(zip(parts_of_speech, match_list))
    
    sub_text_file = text_file
    for part_of_speech, matches in madlib_dict.items():
        vowel_prompt = f'Enter an {part_of_speech.lower()}:\n'
        non_vowel_prompt = f'Enter a {part_of_speech.lower()}:\n'
        for match in range(len(matches)):
            if (len(matches) > 0):
                if part_of_speech == 'ADJECTIVE':
                    matches[match] = input(vowel_prompt)
                    sub_text_file = adj_regex.sub(adj_matches[match], sub_text_file, count=1)
                elif part_of_speech == 'NOUN':
                    matches[match] = input(non_vowel_prompt)
                    sub_text_file = noun_regex.sub(noun_matches[match], sub_text_file, count=1)
                elif part_of_speech == 'ADVERB':
                    matches[match] = input(non_vowel_prompt)
                    sub_text_file = adverb_regex.sub(adverb_matches[match], sub_text_file, count=1)
                elif part_of_speech == 'VERB':
                    matches[match] = input(non_vowel_prompt)
                    sub_text_file = verb_regex.sub(verb_matches[match], sub_text_file, count=1)
                elif part_of_speech == 'ANIMAL':
                    matches[match] = input(non_vowel_prompt)
                    sub_text_file = animal_regex.sub(animal_matches[match], sub_text_file, count=1)
                elif part_of_speech == 'EXCLAMATION':
                    matches[match] = input(non_vowel_prompt)
                    sub_text_file = exclamation_regex.sub(exclamation_matches[match], sub_text_file, count=1)
    
    with open('finished_madlib.txt', 'w') as madlib: 
        for line in sub_text_file:
            madlib.write(line)
    return print(sub_text_file)
 
madlib_generator(read_madlibs)
