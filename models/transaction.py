from database import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)  
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    description = db.Column(db.String(255))