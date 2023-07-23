from models.book import Book

book1 = Book("My Brilliant Friend", "Elena Ferrante", "Fiction")
book2 = Book("1Q84", "Haruki Murakami", "Fiction")
book3 = Book("A little life", "Hanya Yanagihara", "Fiction")
book4 = Book("Everything I Know About Love", "Dolly Alderton", "Self-help")
book5 = Book("Fluent Python: Clear, Concise, and Effective Programming", "Luciano Ramalho", "Computer Science")
book6 = Book("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin", "Computer Science")

books = [book1, book2, book3, book4, book5, book6]

def book_available(book):
    book.checked_out = True    

def book_unavailable(book):
    book.checked_out = False