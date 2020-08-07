"""Seed file to make sample data for users db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

u1 = User(first_name='Ylena', last_name='York')
u2 = User(first_name='Susie', last_name='Queue')
u3 = User(first_name='Jon', last_name='Adams')

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)

db.session.commit()

u1.set_default_img_url()
u2.set_default_img_url()
u3.set_default_img_url()

p1 = Post(title='First Post', content="My very first post", user_id=1)
p2 = Post(title='Second Post', content="My second post", user_id=1)
p3 = Post(title='First Post from Susie', content="My name is Susie", user_id=2)
p4 = Post(title='First Post from Jon', content="Jon wants in on the fun!", user_id=3)
p5 = Post(title='Keep it goin', content="Let us keep the fun a rollin.", user_id=3)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)

db.session.commit()