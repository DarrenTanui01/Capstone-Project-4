from flask import Blueprint, request, jsonify
from database import db
from models.savings import Savings
from models.interest import Interest
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.savings_schema import SavingsSchema
from schemas.interest_schema import InterestSchema

savings_bp = Blueprint('savings', __name__)
savings_schema = SavingsSchema()
interests_schema = InterestSchema(many=True)

@savings_bp.route('/savings', methods=['POST'])
@jwt_required()
def deposit_savings():
    data = request.get_json()
    user_id = get_jwt_identity()
    group_id = data.get('group_id')
    amount = data.get('amount')
    if amount <= 0:
        return jsonify({'error': 'Amount must be positive'}), 400
    savings = Savings.query.filter_by(user_id=user_id, group_id=group_id).first()
    if not savings:
        savings = Savings(user_id=user_id, group_id=group_id, amount=amount)
        db.session.add(savings)
    else:
        savings.amount += amount
    db.session.commit()
    return savings_schema.jsonify(savings), 201

@savings_bp.route('/savings', methods=['GET'])
@jwt_required()
def get_user_savings():
    user_id = get_jwt_identity()
    savings = Savings.query.filter_by(user_id=user_id).all()
    return savings_schema.jsonify(savings, many=True), 200

@savings_bp.route('/savings/<int:group_id>/interest', methods=['POST'])
@jwt_required()
def calculate_interest(group_id):
    data = request.get_json()
    rate = data.get('rate')  # e.g., 0.05 for 5%
    user_id = get_jwt_identity()
    savings = Savings.query.filter_by(user_id=user_id, group_id=group_id).first()
    if not savings:
        return jsonify({'error': 'No savings found for this group'}), 404
    interest_amount = savings.amount * rate
    interest = Interest(savings_id=savings.id, interest_amount=interest_amount, rate=rate)
    db.session.add(interest)
    db.session.commit()
    return InterestSchema().jsonify(interest), 201

@savings_bp.route('/savings/<int:group_id>/interest', methods=['GET'])
@jwt_required()
def get_interest(group_id):
    user_id = get_jwt_identity()
    savings = Savings.query.filter_by(user_id=user_id, group_id=group_id).first()
    if not savings:
        return jsonify({'error': 'No savings found for this group'}), 404
    interests = Interest.query.filter_by(savings_id=savings.id).all()
    return interests_schema.jsonify(interests), 200