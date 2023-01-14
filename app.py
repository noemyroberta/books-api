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


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book_by_id(book_id: int):
    new_book = request.get_json()

    for index, current_book in enumerate(books):
        if current_book.get('id') == book_id:
            books[index].update(new_book)

    return jsonify(f"Livro {new_book.get('title')} alterado com sucesso!")


app.run(port=5000, host='localhost', debug=True)
