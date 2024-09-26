from app import db, Book

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

if __name__ == '__main__':
    init_db()
    print("Database initialized and sample data added.")
