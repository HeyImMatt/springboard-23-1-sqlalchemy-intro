"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

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

    users = User.query.order_by(User.last_name, User.first_name ).all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def add_user():
    """Add user form"""

    if request.method == 'POST':
        req = request.form
        img_url=req['img-url']

        user = User(
          first_name=req['first-name'], 
          last_name=req['last-name'],
          img_url=img_url
          )
          
        try:  
            db.session.add(user)
            db.session.commit()
            if img_url == '':
                user.set_default_img_url()
                db.session.add(user)
                db.session.commit()
        except:
            print('User not added')

        return redirect('/users')

    return render_template('user_form.html')

@app.route('/users/<int:user_id>')
def user_info(user_id):
    """Shows user info"""

    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id)
    return render_template('user_info.html', user=user, posts=posts)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    """Edit user"""

    if request.method == 'POST':
        req = request.form

        user = User.query.get_or_404(user_id)

        img_url=req['img-url']
        
        user.first_name=req['first-name'], 
        user.last_name=req['last-name'],
        user.img_url=img_url
          
        try:  
            db.session.add(user)
            db.session.commit()
            if img_url == '':
                user.set_default_img_url()
                db.session.add(user)
                db.session.commit()
        except:
            print('User not updated')

        return redirect('/users')

    user = User.query.get_or_404(user_id)
    return render_template('user_form.html', user=user, edit_mode=True)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete user"""

    user = User.query.get_or_404(user_id)

    try:  
        db.session.delete(user)
        db.session.commit()
    except:
        print('User not deleted')

    return redirect('/users')

@app.route('/posts/<int:post_id>')
def post_info(post_id):
    """Show post info"""

    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
        
    return render_template('post_info.html', post=post, user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['GET', 'POST'])
def add_post(user_id):
    """Add post form"""

    if request.method == 'POST':
        req = request.form

        post = Post(
          title=req['post-title'], 
          content=req['post-content'],
          user_id=user_id
          )
          
        try:  
            db.session.add(post)
            db.session.commit()
        except:
            print('Post not added')

        return redirect(f'/users/{user_id}')

    return render_template('post_form.html', user_id=user_id)

@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    """Edit post form"""

    if request.method == 'POST':
        req = request.form
        post = Post.query.get_or_404(post_id)

        post.title=req['post-title'], 
        post.content=req['post-content'],
          
        try:  
            db.session.add(post)
            db.session.commit()
        except:
            print('Post not updated')

        return redirect(f'/users/{post.user_id}')

    post = Post.query.get_or_404(post_id)
    return render_template('post_form.html', post=post, edit_mode=True)

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Delete post"""

    post = Post.query.get_or_404(post_id)

    try:  
        db.session.delete(post)
        db.session.commit()
    except:
        print('Post not deleted')

    return redirect(f'/users/{post.user_id}')

@app.route('/tags')
def tags_list():
    """Shows list of all tags"""

    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tags/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    """Edit tag form"""

    if request.method == 'POST':
        req = request.form
        tag = Tag.query.get_or_404(tag_id)

        tag.name=req['tag-name'], 
          
        try:  
            db.session.add(tag)
            db.session.commit()
        except:
            print('Post not updated')

        return redirect(f'/tags/{tag_id}')

    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag_form.html', tag=tag, edit_mode=True)

@app.route('/tags/new', methods=['GET', 'POST'])
def add_tag():
    """Add tag form"""

    if request.method == 'POST':
        req = request.form

        tag = Tag(name=req['tag-name'])
          
        try:  
            db.session.add(tag)
            db.session.commit()
        except:
            print('Post not added')

        return redirect(f'/tags')

    return render_template('tag_form.html')

@app.route('/tags/<int:tag_id>')
def tag_info(tag_id):
    """Shows tag info"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag_info.html', tag=tag)