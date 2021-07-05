# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:50:09 2021

@author: Cleme
"""

#! python3
# date_detection.py - Detects dates in the DD/MM/YYYY format. 

import re

print('Please input a sentence with dates in the DD/MM/YYYY format:')
message = input()

def date_detection(message):
    date_regex = re.compile(r'''(
                ([0-3]?[0-9])           # day
                (\s|-|.|/)             # separator
                ([0-1]?[0-9])           # month
                (\s|-|.|/)             # separator
                ([1-2][0-9][0-9][0-9])  # year 
                            
                            )''', re.VERBOSE)   
    
    # Separtate the match objects in day, month and year
    matches = []
    for group in date_regex.findall(message):
        day_re = group[1]
        month_re = group[3]
        year_re = group[5]
        dates = '/'.join([day_re, month_re, year_re])
        matches.append(dates)
    # month dictionary
    months_dict = {
    'thirty_one_months': ['01', '03', '05', '07', '08', '10', '12'],
    'thirty_months': ['04', '06', '09', '11'],
    'february': '02'}
    
    # Add leading zeros to the front of the days and months if not present
    if len(day_re) == 1:
        day_re = '0' + day_re
    
    if len(month_re) == 1:
        month_re = '0' + month_re
    
    # month rules
    for months, days in months_dict.items():
        if months == 'thirty_one_months':
            for day in days:
                if int(day_re) > 31: 
                    return False
        elif months == 'thirty_months':
            if int(day_re) > 30: 
                for day in days:
                    return False
        # special rules for february
        elif months == 'february':
            if int(day_re) > 29: 
                return False
            elif int(day_re) == 29: 
                # leap year rules
                # 400 year rule holds true least often so it goes first
                if int(year_re) % 400 == 0:
                    return print("Found dates:"), print('\n'.join(matches))
                # 100 year rule means it is not a leap year
                elif int(year_re) % 100 == 0:
                    return False
                # This is the standard 4 year leap year rule and this code will run 
                # if the other exceptions are not true 
                elif int(year_re) % 4 == 0: 
                    return print("Found dates:"), print('\n'.join(matches))
                else: 
                    False
            elif int(day_re) < 29: 
                return print("Found dates:"), print('\n'.join(matches))
        else:
            return print("Found dates:"), print('\n'.join(matches))
# call function
date_detection(message)
                    