
"""
Lore:
The librarian wonders if there is a link between the genres of books and the authors.

Instructions:

Using the provided sample:
What is the favorite genre of author "J.K. Rowling" ?
Which author has the most books in the "Fiction" genre?
Which author has, on average, the longest books (in number of pages)?

Forbidden : use of get() and max()

Hint 1: For the favorite genre, use a dictionary to count the occurrences of each genre for the given author.
Hint 2: For the author with the most books in the "Fiction" genre, use a dictionary to count the occurrences of each author for this genre.
Hint 3: For the author with the longest books, use two dictionaries: one for the sum of pages and one for the number of books per author. Then calculate the average number of pages for each author.
Hint 4: Find the maximum or minimum values in the dictionaries by iterating through the elements.

"""

### Template 

## Test data
books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy", "pages": 500},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "genre": "Fiction", "pages": 96},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction", "pages": 328},
    {"title": "Python for Dummies ", "author": "John Paul Mueller", "genre": "Informatique", "pages": 432},
    {"title": "The Stranger", "author": "Albert Camus", "genre": "Littérature", "pages": 123},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "pages": 1216},
    {"title": "Animal Farm", "author": "George Orwell", "genre": "Fiction", "pages": 112},
]

# Expected result :
# favorite_genre(books, "J.K. Rowling") = "Fantasy"
# fiction_author(books) = "George Orwell"
# long_books_author(books) = "J.R.R. Tolkien"

"""
Complete the functions while keeping their signature
"""

def favorite_genre(books, author):
    # This function returns a string
    return

def fiction_author(books):
    # This function returns a string
    return

def long_books_author(books):
    # This function returns a string
    return

# Solution
def favorite_genre(books, author):
    count_genre = {}
    for book in books:
        if book["author"] == author:
            genre = book["genre"]
            if genre in count_genre:
                count_genre[genre] += 1
            else:
                count_genre[genre] = 1
    # Find the genre with the maximum occurrences
    max_genre = None
    max_count = -1
    for genre, count in count_genre.items():
        if count > max_count:
            max_genre = genre
            max_count = count
    return max_genre

def fiction_author(books):
    count_author = {}
    for book in books:
        if book["genre"] == "Fiction":
            author = book["author"]
            if author in count_author:
                count_author[author] += 1
            else:
                count_author[author] = 1
     # Find the author with the maximum number of "Fiction" books
    max_author = None
    max_count = -1
    for author, count in count_author.items():
        if count > max_count:
            max_author = author
            max_count = count
    return max_author

def long_books_author(books):
    total_pages = {}
    count_books = {}
    for book in books:
        author = book["author"]
        pages = book["pages"]
        if author in total_pages:
            total_pages[author] += pages
            count_books[author] += 1
        else:
            total_pages[author] = pages
            count_books[author] = 1
    avg_pages = {author: total_pages[author] / count_books[author] for author in total_pages}
    # Find the author with the highest average number of pages
    max_author = None
    max_avg = -1
    for author, avg in avg_pages.items():
        if avg > max_avg:
            max_author = author
            max_avg = avg
    return max_author
