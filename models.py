from app import db

class Task(db.Model):  # Capital "M" in db.Model
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    title = db.Column(db.String(100), nullable=False)  # Title is required
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title}'