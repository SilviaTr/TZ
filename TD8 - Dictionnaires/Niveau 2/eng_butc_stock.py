"""
Lore :
The BUTC needs to make an inventory of the books to know how many of each genre they have in stock.

Instructions:
The list stock contains the different genres of books available at the BUTC. 
Each genre can be present in multiple copies. 
Using a dictionary inventory, count the number of books of each genre currently available in the library.

Forbidden : use of get()

Hint 1: Initialize an empty dictionary for the inventory.
Hint 2: Iterate through the list stock with a for loop.
Hint 3: For each genre, check if it is already in the dictionary inventory.
Hint 4: If the genre is already in the dictionary, increment its value by 1.
Hint 5: If the genre is not in the dictionary, add it with a value of 1.

"""

### Template 

## Test data
stock = [ 
    "Fiction", 
    "Computer Science", 
    "Literature", 
    "Fantasy", 
    "Computer Science", 
    "Fiction", 
    "Fantasy", 
    "Literature", 
    "Fiction", 
    "Computer Science", 
    "Fantasy", 
    "Fiction"
]

"""
Complete the function
"""

def make_inventory(stock):
    # This function returns a dictionary
    return 

### Solution
def make_inventory(stock):
    inventory = {}
    for genre in stock:
        if genre in inventory:
            inventory[genre] += 1
        else:
            inventory[genre] = 1
    return inventory
