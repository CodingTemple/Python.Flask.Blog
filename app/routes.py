from app import app
from flask import render_template

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
  return render_template('blog.html')

@app.route('/blog-single')
def blog_single():
  return render_template('blog-single.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

