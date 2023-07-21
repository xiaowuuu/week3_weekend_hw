from flask import Flask, request, Blueprint,render_template
from models.book import Book
from models.book_list import books

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    return render_template("index.jinja", title = "The most borrowed books", book_list = books)

@books_blueprint.route("/books", methods=["POST"])
def add_books():
    book_title = request.form["book_title"]
    author = request.form["author"]
    genre = request.form["genre"]

    new_books = Book(book_title, author, genre)
    books.append(new_books)
    return render_template("index.jinja", title="The most borrowed books", book_list = books)