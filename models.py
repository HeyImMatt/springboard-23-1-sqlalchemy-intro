"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                  primary_key=True,
                  autoincrement=True)
    first_name = db.Column(db.String(50),
                          nullable=False)
    last_name = db.Column(db.String(50),
                          nullable=False)
    img_url = db.Column(db.String(), 
                        nullable=True)
    
    def set_default_img_url(self):
        """Set default profile image url"""
        u = self
        self.img_url = f'https://api.adorable.io/avatars/150/{u.id}.png'
    
    def get_full_name(self): 
        """Return user's full name"""
        u = self
        return f'{u.first_name} {u.last_name}'

    def __repr__(self):
        """Show user info"""
        u = self
        return f'<User {u.id} {u.first_name} {u.last_name} {u.img_url}>'

class Post(db.Model):
    """Post Model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(), nullable=False)
    # Line below worked one day and not the next. WTF. 
    # created_at = db.Column(db.DateTime, default=datetime.now().strftime('%x - %X'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')
    # tags = db.relationship('Tag', secondary='posts_tags', backref='posts')

class Tag(db.Model):
    """Tag Model"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False, unique=True)

    posts = db.relationship('Post', secondary='posts_tags', backref='tags')

class PostTag(db.Model):
    """Post Tags Model"""

    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    