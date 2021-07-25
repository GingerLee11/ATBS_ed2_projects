#!python3
# regex_search.py - Searches all text files in a folder and searches
# for any line that matches a user-supplied regex

import re
from pathlib import Path
import os
import pyinputplus as pyip

def regex_search():

    regex_prompt = 'Please input a regular expression to search text files.\n'

    user_prompt = 'Please input the path to the folder that you would like to search.\n'


    user_regex = pyip.inputRegexStr(regex_prompt)
    user_folder = pyip.inputFilepath(user_prompt)


    for (root, dirs, files) in os.walk(user_folder, topdown=True):
        for file in files:
            if file.endswith('.txt'):
                try:
                    with open(os.path.join(root, file), 'r') as filename:
                        matches = []
                        for line in filename:
                            matches.append(user_regex.findall(line))
                            print(line)

                except FileNotFoundError as error:
                    print(error)

    return print(matches)

regex_search()
