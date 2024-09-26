from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    cover_image = db.Column(db.String(200))

# Routes
@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=20)
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

# Database initialization
def init_db():
    with app.app_context():
        db.create_all()
        # Add some sample data if the database is empty
        if Book.query.count() == 0:
            sample_books = [
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=9.99, cover_image="great_gatsby.jpg"),
                Book(title="To Kill a Mockingbird", author="Harper Lee", price=12.50, cover_image="mockingbird.jpg"),
                Book(title="1984", author="George Orwell", price=10.99, cover_image="1984.jpg"),
            ]
            db.session.add_all(sample_books)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)