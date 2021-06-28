# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:36:43 2021

@author: Cleme
"""

#! python3
# grid_printer.py - Prints out character grids to make pictures

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def grid_printer(grid):
    
    for column in range(len(grid[0])):
        for row in range(len(grid)): 
            print(grid[row][column], end='')
        print()

grid_printer(grid)
