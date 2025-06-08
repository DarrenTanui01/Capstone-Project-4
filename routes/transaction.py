from flask import Blueprint, request, jsonify
from database import db
from models.transaction import Transaction
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.transaction_schema import TransactionSchema

transaction_bp = Blueprint('transaction', __name__)
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

@transaction_bp.route('/transactions', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    user_id = get_jwt_identity()
    group_id = data.get('group_id')
    amount = data.get('amount')
    type_ = data.get('type') 
    description = data.get('description', '')
    if type_ not in ['deposit', 'service_charge']:
        return jsonify({'error': 'Invalid transaction type'}), 400
    transaction = Transaction(
        user_id=user_id,
        group_id=group_id,
        amount=amount,
        type=type_,
        description=description
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction_schema.jsonify(transaction), 201

@transaction_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return transactions_schema.jsonify(transactions), 200

@transaction_bp.route('/transactions/group/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group_transactions(group_id):
    transactions = Transaction.query.filter_by(group_id=group_id).all()
    return transactions_schema.jsonify(transactions), 200