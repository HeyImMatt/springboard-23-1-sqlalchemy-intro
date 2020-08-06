"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

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

    # @classmethod
    # def get_user_by_last_name(cls, last_name):
    #     """Returns list of users ordered by last name"""

    #     return 