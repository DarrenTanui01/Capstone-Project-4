from database import db

class Interest(db.Model):
    __tablename__ = 'interest'
    id = db.Column(db.Integer, primary_key=True)
    savings_id = db.Column(db.Integer, db.ForeignKey('savings.id'), nullable=False)
    interest_amount = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    calculated_on = db.Column(db.DateTime, server_default=db.func.now())