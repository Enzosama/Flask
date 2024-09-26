from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config
import bcrypt
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self,username,email,password,name):
        self.name = name
        self.username = username
        self.email = email
        # self.password = 
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    cover_image = db.Column(db.String(200))

# @app.route('/home')
# def home():
#     if 'email' or 'username' not in session:
#         user = User.query.filter_by(email=session['email' or 'username']).first()
#         return render_template('index.html', user=user)

#     return redirect('/login')

# @app.route('/logout')
# def logout():
#     session.pop('email' and 'username', None)
#     return redirect('/login')

def init_db():
    db.create_all()

    if Book.query.count() == 0:
        sample_books = [
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=9.99, cover_image="static/data/5-phuong-thuc-ghi-nhan-no-luc-cua-nhan-vien-gary-chapman-paul-white-450x658.jpg"),
            Book(title="To Kill a Mockingbird", author="Harper Lee", price=12.50, cover_image="static/data/dac-nhan-tam-prc-pdf-epub.jpg"),
            Book(title="1984", author="George Orwell", price=10.99, cover_image="static/data/nghin-le-mot-dem-dan-gian-a-rap-442x680.jpg"),
        ]
        db.session.add_all(sample_books)
        db.session.commit()
        print("Sample data added.")


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
    with app.app_context():
        init_db()
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8888)))
