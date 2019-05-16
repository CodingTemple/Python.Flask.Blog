from app import db, Login
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100), index=True, unique=True)
  posts = db.relationship('Post', backref="author", lazy="dynamic")

  def __repr__(self):
    return f"{self.name} | {self.email}"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150))
  image = db.Column(db.String(250), nullable=True)
  body = db.Column(db.Text)
  created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  comments = db.relationship('Comment', backref="comment", lazy="dynamic")

  def __repr__(self):
    return f"{self.user_id} | {self.title}"

class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(100), index=True)
  body = db.Column(db.Text)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
  created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self):
    return f"{self.email} | {self.body[:50]}..."
