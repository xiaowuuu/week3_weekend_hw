from flask import Flask, request, Blueprint,render_template,redirect
from models.book import Book
from models.book_list import books, book_available, book_unavailable

books_blueprint = Blueprint("books", __name__)

# list all the books
@books_blueprint.route("/books")
def index():
    return render_template("index.jinja", title = "New & Trending", book_list = books)

# show individual book
@books_blueprint.route("/books/<index>")
def individual_book(index):
        # return render_template("individual_book.jinja", title = books[int(index)].book_title, book_list = books)
    return render_template("individual_book.jinja", title = books[int(index)].book_title, book = books[int(index)])

# add new books
@books_blueprint.route("/books", methods=["POST", "GET"])
def add_books():
    book_title = request.form["book_title"]
    author = request.form["author"]
    genre = request.form["genre"]


    new_books = Book(book_title, author, genre)
    books.append(new_books)
    # return render_template("index.jinja", title="The most borrowed books", book_list = books)
    return redirect("/books")

# remove a book from library
@books_blueprint.route("/books/delete/<index>", methods=["GET","POST"])
def remove_book(index):
    books.remove(books[int(index)])
    return redirect("/books")

# borrow a book
@books_blueprint.route("/books/rent/<index>", methods=["GET","POST"])
def borrow_book(index):
    book_available(books[int(index)])
    return redirect("/books")

# return a book
@books_blueprint.route("/books/return/<index>", methods=["POST"])
def return_book(index):
    book_available(books[int(index)])
    return redirect("/books")