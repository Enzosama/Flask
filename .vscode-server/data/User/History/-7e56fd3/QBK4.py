def load_sample_data(db, Book):
    sample_books = [
        Book(title="5 Phương Thức Ghi Nhận Nỗ Lực Của Nhân Viên", author="Gary Chapman", price=101150, cover_image="static/data/5-phuong-thuc-ghi-nhan-no-luc-cua-nhan-vien-gary-chapman-paul-white-450x658.jpg"),
        Book(title="Đắc Nhân Tâm", author="Dale Carnegie", price=72000, cover_image="static/data/dac-nhan-tam-prc-pdf-epub.jpg"),
        Book(title="Nghìn lẻ một đêm", author="Antoine Galland", price=80000, cover_image="static/data/nghin-le-mot-dem-dan-gian-a-rap-442x680.jpg"),
        Book(title="Tôi muốn đi sờ cá ở cục yêu quái", author="Giang Nguyệt Niên Niên", price=50000, cover_image="static/data/toi-muon-di-so-ca-o-cuc-yeu-quai-giang-nguyet-nien-nien-450x675.jpg"),
    ]
    
    for sample_book in sample_books:
        existing_book = Book.query.filter_by(title=sample_book.title).first()
        if existing_book:
            existing_book.author = sample_book.author
            existing_book.price = sample_book.price
            existing_book.cover_image = sample_book.cover_image
        else:
            db.session.add(sample_book)
    
    db.session.commit()
    print("Sample data updated.")

if __name__ == '__main__':
    pass