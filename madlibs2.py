#! python3
# madlibs.py - Mad Libs program that reads in text files and lets users 
# add input anywhere any of the madlib words show up in the text

import os
from pathlib import Path
import re

# Example madlib
text = 'The ADJECTIVE ANIMAL PAST-TENSE-VERB into the ADJECTIVE bar, and PAST-TENSE-VERB a(n) NOUN.'

path = 'Your path here'

os.chdir(path)

with open('madlibs.txt', 'r') as madlibs: 
    read_madlibs = madlibs.read()

def madlib_generator(text_file):

    # Define words that would be used in madlibs
    madlib_words = [
        'ADJECTIVE',
        'NAME',
        # The same matching problem with verbs is going to occur with 
        # nouns and plural nouns
        'PLURAL NOUN',
        'NOUN',
        'ADVERB',
        'PAST-TENSE-VERB',
        '-ING-VERB',
        # Verb still matches to the Past Tense Verbs
        # When spaces are used to specify the verb match then the spaces are 
        # matched and there are not spaces when printed
        'PRESENT-TENSE-VERB',
        'ANIMAL',
        'EXCLAMATION',
        'LOCATION',
        'CITY',
        'DAY OF THE WEEK',
        'TIME',
        'NUMBER',
        'BODY PART',

            ]

    vowels = (
        'A', 'I', 'E', 'O', 'U'
            )

    # Create a dictionary that has the regex as keys and the matches as values
    regex_matches = {}
    sub_text = text
    for word in madlib_words:
        regex = re.compile(word)
        regex_matches[regex] = regex.findall(text)
    # Loop through the dictionary so that the user can input their values for the madlib words
    for regex, matches in regex_matches.items():
        # Skips the word if there are no matches
        if len(matches) == 0:
            continue
        # Loops through each match in range of the total matches for each madlib word
        for match in range(len(matches)):
            # 'a' for words that start with a consonant 
            # 'an for words that start with a vowel
            vowel_prompt = f'Enter an {(matches[match].lower().strip())}:\n'
            non_vowel_prompt = f'Enter a {(matches[match].lower().strip())}:\n'
            # Vowel and non-vowel logic
            if matches[match].startswith(vowels, 0, 2):
                matches[match] = input(vowel_prompt)
                sub_text = regex.sub(matches[match], sub_text, count=1)
            else:
                matches[match] = input(non_vowel_prompt)
                sub_text = regex.sub(matches[match], sub_text, count=1)
    
    with open('finished_madlib.txt', 'w') as madlib: 
        for line in sub_text:
            madlib.write(line)
    return print(sub_text)   

# Example madlib
madlib_generator(text)

# Takes in text files and returns madlibs  
#madlib_generator(read_madlibs)
