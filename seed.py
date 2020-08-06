"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

u1 = User(first_name='Jon', last_name='Adams')
u2 = User(first_name='Susie', last_name='Queue')
u3 = User(first_name='Ylena', last_name='York')

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)

db.session.commit()

u1.set_default_img_url()
u2.set_default_img_url()
u3.set_default_img_url()

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)

db.session.commit()