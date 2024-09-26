from flask_sqlalchemy import SQLAlchemy
from app import db, Book  # Import from app.py
import os

def init_db():
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
    print("Database initialized and sample data added.")
