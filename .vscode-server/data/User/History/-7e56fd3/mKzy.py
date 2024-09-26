from app import db, Book

def init_db():
    db.create_all()

    sample_books = [
        Book(title=" 5 Phương Thức Ghi Nhận Nỗ Lực Của Nhân Viên", author="Gary Chapman", price=101.150, cover_image="static/data/5-phuong-thuc-ghi-nhan-no-luc-cua-nhan-vien-gary-chapman-paul-white-450x658.jpg"),
        Book(title=" Đắc Nhân Tâm", author="Dale Breckenridge Carnegie", price=72.000, cover_image="static/data/dac-nhan-tam-prc-pdf-epub.jpg"),
        Book(title="Nghìn lẻ một đêm", author="Antoine Galland", price=80.000, cover_image="static/data/nghin-le-mot-dem-dan-gian-a-rap-442x680.jpg"),
    ]
    
    # Check if we need to add sample books
    if Book.query.count() < len(sample_books):
        db.session.add_all(sample_books)
        db.session.commit()
        
        
if __name__ == '__main__':
    init_db()
    print("Database initialized and sample data added.")
