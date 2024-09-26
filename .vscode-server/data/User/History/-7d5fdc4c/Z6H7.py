from app import db, Book

def init_db():
    db.create_all()

    sample_books = [
        Book(title="5 Phương Thức Ghi Nhận Nỗ Lực Của Nhân Viên", author="Gary Chapman", price=101.150, cover_image="static/data/5-phuong-thuc-ghi-nhan-no-luc-cua-nhan-vien-gary-chapman-paul-white-450x658.jpg"),
        Book(title="Đắc Nhân Tâm", author="Dale Carnegie", price=72.000, cover_image="static/data/dac-nhan-tam-prc-pdf-epub.jpg"),
        Book(title="Nghìn lẻ một đêm", author="Antoine Galland", price=80.000, cover_image="static/data/nghin-le-mot-dem-dan-gian-a-rap-442x680.jpg"),
        Book(title="Tôi muốn đi sờ cá ở cục yêu quái", author="Giang Nguyệt Niên Niên", price=50.000, cover_image="/teamspace/studios/this_studio/static/data/toi-muon-di-so-ca-o-cuc-yeu-quai-giang-nguyet-nien-nien-450x675.jpg"),
    ]
    
    # Check existing books
    existing_titles = {book.title for book in Book.query.all()}
    
    # Add missing sample books
    for sample_book in sample_books:
        if sample_book.title not in existing_titles:
            db.session.add(sample_book)
    
    db.session.commit()
    print("Database initialized and sample data added if necessary.")

if __name__ == '__main__':
    init_db()
