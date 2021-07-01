# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 07:35:33 2021

@author: Cleme
"""

#! python3
# table_printer.py - Takes a list of strings and displays it as a neat table

table_data = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

# function that prints neatly prints a table of data
def print_table(table_data):
    # Creates an indexing variable
    i = -1
    # sets the column widths to zero
    col_width = [0] * len(table_data)
    # loop through the lines in the table data to find the longest string
    for line in table_data:
        i += 1
        for word in line:
            # If word is longer than the current longest word, take the length
            # of that word and put it into col_width at index i
            if len(word) > col_width[i]:
                col_width[i] = len(word)
    # method to rotate the table (learned in chapter 4) and print
    for line in range(len(table_data[0])):
        for word in range(len(table_data)):
            print(table_data[word][line].rjust(col_width[word], ' '), end=' ')
        print()   
# execute function           
print_table(table_data)
