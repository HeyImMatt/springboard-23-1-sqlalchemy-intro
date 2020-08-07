"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "blogly1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """Redirects to users list"""

    return redirect('/users')

@app.route('/users')
def users_list():
    """Shows list of all users"""

    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def user_info(user_id):
    """Shows user info"""

    user = User.query.get_or_404(user_id)
    return render_template('user_info.html', user=user)

@app.route('/users/new')
def add_user():
    """Add user form"""

    return render_template('user_form.html')