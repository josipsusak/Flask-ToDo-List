from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create entry list table
class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(250), nullable=False)
    added_date = db.Column(db.String(100))
    due_date = db.Column(db.String(15))
    finished = db.Column(db.Boolean, default=False)
