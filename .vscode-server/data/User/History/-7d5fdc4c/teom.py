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

# Function to initialize and add data
def init_db():
    db.create_all()

    # Add some sample data if the database is empty
    if Book.query.count() == 0:
        sample_books = [
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=9.99, cover_image="static/data/5-phuong-thuc-ghi-nhan-no-luc-cua-nhan-vien-gary-chapman-paul-white-450x658.jpg"),
            Book(title="To Kill a Mockingbird", author="Harper Lee", price=12.50, cover_image="static/data/dac-nhan-tam-prc-pdf-epub.jpg"),
            Book(title="1984", author="George Orwell", price=10.99, cover_image="static/data/nghin-le-mot-dem-dan-gian-a-rap-442x680.jpg"),
        ]
        db.session.add_all(sample_books)
        db.session.commit()
        print("Sample data added.")

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

if __name__ == '__main__':
    # Initialize the database and add data before starting the app
    with app.app_context():
        init_db()
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8888)))
