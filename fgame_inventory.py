# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 07:29:15 2021

@author: Cleme
"""

#!python3 
# display_inventory.py - Take in a dictionary representing a player's inventory 
# and display it to the the screen

# displays player inventory
def display_inventory(inventory):
        print("Inventory:")
        item_total = 0 
        for k, v in inventory.items(): 
            # adds the value from each key for the total
            item_total = item_total + v
            print('{}  {}'.format(v, k))
        print("Total number of items: " + str(item_total))

# adds loot to the current player inventory
def add_to_inventory(inventory, added_items):
    # loops through the loot list
    for item in added_items:
        # if key already exists, add 1 to value
        if item in inventory.keys(): 
            inventory[item] += 1
        # if key doesn't exist, create a key and set the value equal to 1
        if item not in inventory.keys(): 
            inventory[item] = 1
            
    return inventory

# player inventory
stuff = {'enchanted robes': 1, 'staff of resurrection': 1, 'torch': 4, 'lockpicks': 2, 'gold coin': 15}
display_inventory(stuff)

# loot
dragon_loot = ['gold coin', 'dragon scales', 'dagger', 'gold coin', 'gold coin', 'sapphire', 'ruby', 'dagger']

# add the loot to the inv and then display the inv again
stuff = add_to_inventory(stuff, dragon_loot)        
display_inventory(stuff)
