from flask import Flask, jsonify, request
from books_data import books

app = Flask(__name__)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id: int):
    for book in books:
        if book.get('id') == book_id:
            return jsonify(book)


app.run(port=5000, host='localhost', debug=True)
