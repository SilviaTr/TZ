"""
Lore:
The BUTC wants to recommend books to readers based on their preferences.

Instructions:
Write a function that recommends the first book that matches the reader's preferences based on 3 characteristics (preferred genre, preferred author, preferred length). 
The characteristics of the available books are provided. In case of a tie, apply the following priority: genre > author > length.

Forbidden : use of get()

Hint 1: Iterate through the list of books with a for loop.
Hint 2: First check if the genre of the book matches the preferred genre.
Hint 3: If no book matches the preferred genre, check if the author of the book matches the preferred author.
Hint 4: If no book matches the preferred author, check if the length of the book matches the preferred length.
Hint 5: Return the title of the first book that matches one of the preferences, respecting the order of priority.

"""


### Template 

## Test data
books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy", "pages": 500, "length": "medium"},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "genre": "Fiction", "pages": 96, "length": "short"},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction", "pages": 328, "length": "medium"},
    {"title": "Python for Dummies ", "author": "John Paul Mueller", "genre": "Informatique", "pages": 432, "length": "medium"},
    {"title": "The Stranger", "author": "Albert Camus", "genre": "Littérature", "pages": 123, "length": "short"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "pages": 1216, "length": "long"},
    {"title": "Animal Farm", "author": "George Orwell", "genre": "Fiction", "pages": 112, "length": "short"},
]


"""
Complete the function
"""
def recommend_book(preferred_genre, preferred_author, preferred_length):
    # This function returns a string (the title of the recommended book)
    return 

# Expected result :
# recommend_book('Fiction', 'George Orwell', 'short') = 'The Little Prince'
# recommend_book('Art', 'George Orwell', 'long') = '1984' 
# recommend_book('Art', 'Art Test', 'long') = 'The Lord of the Rings'
# recommend_book('Art', 'Recueil', 'very short') = 'No book matches your preferences'

### Solution
def recommend_book(preferred_genre, preferred_author, preferred_length):
    for book in books:
        if book["genre"] == preferred_genre:
            return book["title"]
        if book["author"] == preferred_author:
            return book["title"]
        if book["length"] == preferred_length:
            return book["title"]
    return "No book matches your preferences"



