#! python3
#sandwich_maker.py - Asks users for their sandwich preferences

import pyinputplus as pyip

# sandwich maker function
def sandwich_maker():
    # Set the total initial cost to 0
    total_cost = 0
    #ingredient dictionaries
    bread_prices = {
                    'wheat': 2.25,
                    'white': 2.00,
                    'sourdough': 2.50
                    }
    bread_choices = []
    for bread in bread_prices.keys():
        bread_choices.append(bread)
    protein_prices = {
                    'chicken': 2.00,
                    'meatball': 2.50,
                    'turkey': 2.50,
                    'ham': 2.00,
                    'tofu': 1.50,
                    'veggie burger': 2.00
                    }
    protein_choices = []
    for protein in protein_prices.keys():
        protein_choices.append(protein)

    cheese_prices = {
                    'cheddar': 1.00,
                    'Swiss': 1.00,
                    'Mozzarella': 1.25
                    }
    cheese_choices = []
    for cheese in cheese_prices.keys():
        cheese_choices.append(cheese)

    condiment_prices = {
                    'Mayo': 0.10,
                    'Mustard': 0.10,
                    'BBQ sauce': 0.15,
                    'Truffle sauce': 1.00,
                    'Guac': 1.50,
                    'Tomato sauce': 0.50,
                    'Hoisin sauce': 0.15
                    }
    condiment_choices = []
    for condiment in condiment_prices.keys():
        condiment_choices.append(condiment)

    vegetable_prices = {
                    'lettuce': 0.10,
                    'tomato': 0.10,
                    'pickles': 0.05,
                    'cucumber': 0.10,
                    'red onion': 0.05,
                    'spinach': 0.10,
                    'avocado': 0.15
                    }
    vegetable_choices = []
    for vegetable in vegetable_prices.keys():
        vegetable_choices.append(vegetable)

    # Ask the user for their sandwich preferences using inputMenu()
    print('Welcome to the "Ginger" breadman sandwich shop!')
    # Ask for number of sandwiches and generate a for loop based on the ans
    num_sandwiches = pyip.inputInt('How many sandwiches would you like?', min=1)
    for sandwich in range(num_sandwiches):
        print(f"Please select what you would like on your sandwich. This is sandwich number {sandwich+1}.")
        # Bread menu options and price
        bread_choice = pyip.inputMenu(bread_choices)
        for bread, price in bread_prices.items():
            if bread_choice == bread:
                total_cost += price
        # Protein menu options and price
        protein_choice = pyip.inputMenu(protein_choices)
        for protein, price in protein_prices.items():
            if protein_choice == protein:
                total_cost += price
        # Ask user first if they want cheese then gives options
        cheese_prompt = 'Would you like cheese?'
        cheese_Q = pyip.inputYesNo(cheese_prompt, yesVal='yes', noVal='no')
        if cheese_Q == 'yes':
            cheese_choice = pyip.inputMenu(cheese_choices)
            for cheese, price in cheese_prices.items():
                if cheese_choice == cheese:
                    total_cost += price

        # Collects yes or no condiment responses
        condiment_responses = {}
        for condiment in condiment_choices:
            condiment_prompt = (f'Would you like {condiment}?\n')
            condiment_responses[condiment] = (pyip.inputYesNo(condiment_prompt))
        # Loops through both dictionaries to compare values
        for condiment_r, response in condiment_responses.items():
            if response == "yes":
                for condiment_p, price in condiment_prices.items():
                    if condiment_r == condiment_p:
                        total_cost += price
        #  Collects yes or no responses
        vegetable_responses = {}
        for vegetable in vegetable_choices:
            vegetable_prompt = (f'Would you like {vegetable}?\n')
            vegetable_responses[vegetable] = (pyip.inputYesNo(vegetable_prompt))

        # Loops through both dictionaries to compare values
        for vegetable_r, response in vegetable_responses.items():
            if response == "yes":
                for vegetable_p, price in vegetable_prices.items():
                    if vegetable_r == vegetable_p:
                        total_cost += price

    return print(f" Your total cost is ${round(total_cost, 2)}.")

sandwich_maker()
