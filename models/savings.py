from database import db

class Savings(db.Model):
    __tablename__ = 'savings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())