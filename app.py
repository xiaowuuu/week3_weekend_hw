from flask import Flask
from controller.book_controller import books_blueprint
app = Flask(__name__)
app.register_blueprint(books_blueprint)
@app.route("/")
def welcome():
    return "<h1>Welcome to the Library.</h1>"

