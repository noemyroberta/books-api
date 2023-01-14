from flask import Flask, jsonify, request
from books_data import books

app = Flask(__name__)


@app.route('/books')
def get_books():
    return jsonify(books)
