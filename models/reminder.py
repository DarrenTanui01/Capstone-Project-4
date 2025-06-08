from database import db

class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean, default=False)