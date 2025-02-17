"""
Lore
The library wishes to organize a contest to reward the most appreciated books by readers. The books will be judged on several criteria:
- Average rating
- Number of votes
- Category
 
The criteria for selecting the winning books are as follows:
- For each category, select the book with the highest average rating.
- In case of a tie in average rating, select the book with the highest number of votes.
- In case of a tie in votes, select the oldest book (with the lowest year of publication).
 
Instructions:
Write a function that takes a list of dictionaries representing the books as input. Each dictionary describes a book by its title, author, category, average rating, number of votes, and year of publication. 
This function should return a dictionary where each key is a category and the associated value is the winning book of that category according to the criteria described above.
 
Forbidden: use of sorted()
 
Hint 1: For each category, use a dictionary to store the books of that category.
Hint 2: For each category, go through the list of books to find the winning book according to the criteria.
Hint 3: Go through the list of books once to group them by category, then a second time to determine the winner of each category.
Hint 4: Be careful to respect the selection criteria.
"""

### Template 
 
# Test data
books = [ 
    {"title": "Harry Potter", "author": "J.K. Rowling", "category": "Fantasy", "average_rating": 4.9, "votes": 1000000, "year": 1997}, 
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "category": "Fiction", "average_rating": 4.8, "votes": 500000, "year": 1943}, 
    {"title": "1984", "author": "George Orwell", "category": "Fiction", "average_rating": 4.8, "votes": 600000, "year": 1949}, 
    {"title": "Python for Dummies", "author": "John Paul Mueller", "category": "Computer Science", "average_rating": 4.5, "votes": 250000, "year": 2015}, 
    {"title": "The Stranger", "author": "Albert Camus", "category": "Literature", "average_rating": 4.3, "votes": 300000, "year": 1942}, 
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "average_rating": 4.9, "votes": 800000, "year": 1954}, 
    {"title": "Animal Farm", "author": "George Orwell", "category": "Fiction", "average_rating": 4.7, "votes": 400000, "year": 1945} 
]


# Expected result :
"""
winning_books(books) = {
    'Fantasy': {'title': 'Harry Potter', 'author': 'J.K. Rowling', 'category': 'Fantasy', 'average_rating': 4.9, 'votes': 1000000, 'year': 1997}, 
    'Fiction': {'title': 'The Little Prince', 'author': 'Antoine de Saint-Exupéry', 'category': 'Fiction', 'average_rating': 4.8, 'votes': 500000, 'year': 1943}, 
    'Computer Science': {'title': 'Python for Dummies', 'author': 'John Paul Mueller', 'category': 'Computer Science', 'average_rating': 4.5, 'votes': 250000, 'year': 2015}, 
    'Literature': {'title': 'The Stranger', 'author': 'Albert Camus', 'category': 'Literature', 'average_rating': 4.3, 'votes': 300000, 'year': 1942}
}
"""

"""
Complete the function 
"""
 
def winning_books(books): 
    # This function returns a dictionary 
    return

### Solution
def winning_books(books): 
    categories = {} 
    for book in books: 
        category = book["category"] 
        if category not in categories: 
            categories[category] = [] 
        categories[category].append(book)
    winners = {}
    for category, books_list in categories.items():
        best_book = books_list[0]
        for book in books_list:
            if (
                book["average_rating"] > best_book["average_rating"] or
                (book["average_rating"] == best_book["average_rating"] and book["votes"] > best_book["votes"]) or
                (book["average_rating"] == best_book["average_rating"] and book["votes"] == best_book["votes"] and book["year"] < best_book["year"])
            ):
                best_book = book
        winners[category] = best_book
    return winners
