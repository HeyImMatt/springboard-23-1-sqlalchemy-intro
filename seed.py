"""Seed file to make sample data for users db."""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

u1 = User(first_name='Ylena', last_name='York')
u2 = User(first_name='Susie', last_name='Queue')
u3 = User(first_name='Jon', last_name='Adams')

db.session.add_all([u1, u2, u3])

# Commit users before other actions so there are IDs
db.session.commit()

u1.set_default_img_url()
u2.set_default_img_url()
u3.set_default_img_url()

p1 = Post(title='First Post', content="My very first post", user_id=1)
p2 = Post(title='Second Post', content="My second post", user_id=1)
p3 = Post(title='First Post from Susie', content="My name is Susie", user_id=2)
p4 = Post(title='First Post from Jon', content="Jon wants in on the fun!", user_id=3)
p5 = Post(title='Keep it goin', content="Let us keep the fun a rollin.", user_id=3)

t1 = Tag(name='firstpost')
t2 = Tag(name='cool')
t3 = Tag(name='funny')
t4 = Tag(name='controversial')

db.session.add_all([u1, u2, u3, p1, p2, p3, p4, p5, t1, t2, t3, t4])
db.session.commit()

# Add tags to posts
pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=1, tag_id=2)
pt3 = PostTag(post_id=2, tag_id=3)
pt4 = PostTag(post_id=2, tag_id=1)

db.session.add_all([pt1, pt2, pt3, pt4])
db.session.commit()