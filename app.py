from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Corrected database URI (note: use one '=' sign)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect to the database
db = SQLAlchemy(app)

# User model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)  # use String for passwords

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def home():
    return render_template('home.html')


# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        raw_password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, raw_password):
            return render_template('welcome.html', name=user.name)
        else:
            return "Invalid email or password."

    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        raw_password = request.form.get('password')

        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists. Please log in."

        # Hash the password before storing
        hashed_password = generate_password_hash(raw_password)

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('signup.html')



@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
