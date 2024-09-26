from flask import Flask, render_template, request, session, redirect, url_for
from config import Config
from middle_secure import auth
import bcrypt
import os
from models import db, User, Book
from data_loader import load_sample_data

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/logout')
@auth
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            return redirect(url_for('home'))
        
        return render_template('login.html', error="Invalid email or password")
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('register.html', error="Email is already in use.")
        
        new_user = User(username=username, email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        session['email'] = new_user.email
        return redirect(url_for('home'))
    
    return render_template('register.html')

#Quản trị account
@app.route('/sitemanager', methods=['GET', 'POST'])
def sitemanager():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['admin'] = True
            return redirect(url_for('site_manager_dashboard'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('sitemanager.html')

@app.route('/site_manager_dashboard')
def site_manager_dashboard():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    users_count = User.query.count()
    books_count = Book.query.count()
    return render_template('site_manager_dashboard.html', users_count=users_count, books_count=books_count)

@app.route('/site_manager_users')
def site_manager_users():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    users = User.query.all()
    return render_template('site_manager_users.html', users=users)

@app.route('/site_manager_user/add', methods=['POST'])
def site_manager_add_user():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    new_user = User(username=username, email=email, password=password, name=username)
    db.session.add(new_user)
    db.session.commit()
    flash("User added successfully", "success")
    return redirect(url_for('site_manager_users'))

@app.route('/site_manager_user/edit/<int:user_id>', methods=['GET', 'POST'])
def site_manager_edit_user(user_id):
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        if request.form['password']:
            user.password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        db.session.commit()
        flash("User updated successfully", "success")
        return redirect(url_for('site_manager_users'))
    return render_template('site_manager_edit_user.html', user=user)

@app.route('/site_manager_user/delete/<int:user_id>', methods=['POST'])
def site_manager_delete_user(user_id):
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully", "success")
    return redirect(url_for('site_manager_users'))

@app.route('/site_manager_books')
def site_manager_books():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    books = Book.query.all()
    return render_template('site_manager_books.html', books=books)

@app.route('/site_manager_book/add', methods=['GET', 'POST'])
def site_manager_add_book():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            price=float(request.form['price']),
            cover_image=request.form['cover_image']
        )
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully", "success")
        return redirect(url_for('site_manager_books'))
    return render_template('site_manager_add_book.html')

@app.route('/site_manager_book/edit/<int:book_id>', methods=['GET', 'POST'])
def site_manager_edit_book(book_id):
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.price = float(request.form['price'])
        book.cover_image = request.form['cover_image']
        db.session.commit()
        flash("Book updated successfully", "success")
        return redirect(url_for('site_manager_books'))
    return render_template('site_manager_edit_book.html', book=book)

@app.route('/site_manager_book/delete/<int:book_id>', methods=['POST'])
def site_manager_delete_book(book_id):
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Book deleted successfully", "success")
    return redirect(url_for('site_manager_books'))



@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=20)
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

@app.route('/profile')
@auth
def profile():
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

def init_db():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        load_sample_data()
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
