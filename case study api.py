from flask import Flask, request, jsonify
app = Flask(__name__)

# Sample of data to simulate a database
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"},
]

# CRUD operations

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({"message": "Book added successfully"}), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book)

# Update a book by ID
@app.route('books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    book.update(request.json)
    return jsonify({"message": "Book updated successfully"})

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    books.remove(books)
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
                        