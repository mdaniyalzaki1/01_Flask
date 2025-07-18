# Flask Login & Signup App 🔐

A minimal Flask web application with user registration and login functionality using SQLite and SQLAlchemy. Includes password hashing, user authentication, and a simple user list page.

## 🚀 Features

- User Signup with hashed passwords 🔒
- Login with email & password
- Welcome page after login
- View all registered users
- Styled with CSS (clean & minimal)

## 🛠️ Tech Stack

- **Flask** (Python Web Framework)
- **SQLite** (Database)
- **SQLAlchemy** (ORM)
- **Jinja2** (Templating)
- **HTML/CSS**

## 📂 Project Structure

```
01_basic_flask_login/
│
├── app.py                 # Main Flask application
├── init_db.py             # (Optional) Script to init database
├── instance/
│   └── database.db        # SQLite database
├── static/
│   └── styles.css         # Custom CSS
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── welcome.html
│   └── users.html
```

## ▶️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/mdaniyalzaki1/01_Flask.git
cd 01_Flask
```

2. Create virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install flask flask_sqlalchemy werkzeug
```

4. Run the app:

```bash
python app.py
```

Then visit: `http://127.0.0.1:5000`
