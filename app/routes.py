from app import app
from flask import render_template
from app.models import User, Post, Comment

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
  return render_template('blog.html', **context)

@app.route('/blog/<int:id>', methods=['GET', 'POST'])
def blog_single(id):
  context = {
    'post': Post.query.get(id)
  }
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

