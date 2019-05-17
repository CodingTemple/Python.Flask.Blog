from app import app, db
from flask import render_template, url_for, redirect
from app.models import User, Post, Comment
from app.forms import CommentForm

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')

@app.route('/pricing')
def pricing():
  return render_template('pricing.html')

@app.route('/blog')
def blog():
  context = {
    'posts': Post.query.all()
  }
  return render_template('blog.html', **context)

@app.route('/blog/<int:id>', methods=['GET', 'POST'])
def blog_single(id):
  form = CommentForm()
  context = {
    'post': Post.query.get(id),
    'form': form,
    'comments': Post.query.get(id).comments.all()
  }
  if form.validate_on_submit():
    db.session.add(Comment(name=form.name.data, email=form.email.data, body=form.body.data, post_id=id))
    db.session.commit()
    return redirect(url_for('blog_single', id=id, _anchor='section-comments'))
  return render_template('blog-single.html', **context)

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/admin')
def admin():
  return render_template('admin.html')

