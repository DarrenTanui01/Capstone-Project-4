from flask import Blueprint, request, jsonify
from database import db
from models.message import Message
from models.reminder import Reminder
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.message_schema import MessageSchema
from schemas.reminder_schema import ReminderSchema
from datetime import datetime

communication_bp = Blueprint('communication', __name__)
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
reminder_schema = ReminderSchema()
reminders_schema = ReminderSchema(many=True)


@communication_bp.route('/messages', methods=['POST'])
@jwt_required()
def send_message():
    data = request.get_json()
    sender_id = get_jwt_identity()
    group_id = data.get('group_id')
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Message content required'}), 400
    message = Message(group_id=group_id, sender_id=sender_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message_schema.jsonify(message), 201


@communication_bp.route('/messages/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group_messages(group_id):
    messages = Message.query.filter_by(group_id=group_id).order_by(Message.timestamp.desc()).all()
    return messages_schema.jsonify(messages), 200

# Create a reminder
@communication_bp.route('/reminders', methods=['POST'])
@jwt_required()
def create_reminder():
    data = request.get_json()
    user_id = get_jwt_identity()
    group_id = data.get('group_id')
    message = data.get('message')
    due_date_str = data.get('due_date')
    try:
        due_date = datetime.fromisoformat(due_date_str)
    except Exception:
        return jsonify({'error': 'Invalid date format. Use ISO format.'}), 400
    reminder = Reminder(user_id=user_id, group_id=group_id, message=message, due_date=due_date)
    db.session.add(reminder)
    db.session.commit()
    return reminder_schema.jsonify(reminder), 201


@communication_bp.route('/reminders', methods=['GET'])
@jwt_required()
def get_reminders():
    user_id = get_jwt_identity()
    reminders = Reminder.query.filter_by(user_id=user_id).order_by(Reminder.due_date).all()
    return reminders_schema.jsonify(reminders), 200