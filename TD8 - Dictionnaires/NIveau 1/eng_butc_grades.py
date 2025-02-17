"""
Lore:
The literary critics' ratings are available! What rating did each book receive?

Instructions:
Write a function that takes as input the dictionary ratings and the string book_title. 
This function returns the rating of the book based on the key book_title. 
If the book is not in the dictionary, it returns -1.

Forbidden : use of get()

Hint 1: Use the 'in' operator to check if a key exists in the dictionary.
Hint 2: If the key exists, use dictionary[key] to get the associated value.
Hint 3: If the key does not exist, return -1.
Hint 4: Use an if-else conditional structure to handle both cases.

"""

### Template 

## Test data
ratings = { 
    "The Little Prince": 9, 
    "Python for Dummies": 7, 
    "The Stranger": 8, 
    "The Lord of the Rings": 10, 
    "1984": 9, 
    "Harry Potter": 10
}

book_title = "L'Étranger"
# Expected result: search_book_rating(ratings, book_title) = 8

book_title = "Le Hobbit"
# Expected result: search_book_rating(ratings, book_title) = -1

"""
Complete the function 
"""

def search_book_rating(ratings, book_title):
    # This function returns an integer
    return

### Solution
def search_book_rating(ratings, book_title):
    if book_title in ratings:
        return ratings[book_title]
    else:
        return -1
