from app import app, db
from app.models import User, Comment, Post

@app.shell_context_processor
def shell_context():
  return {
    'db': db,
    'User': User,
    'Comment': Comment,
    'Post': Post,
  }