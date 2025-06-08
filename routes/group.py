from flask import Blueprint, request, jsonify
from database import db
from models.group import Group
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.group_schema import GroupSchema

group_bp = Blueprint('group', __name__)
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

@group_bp.route('/groups', methods=['POST'])
@jwt_required()
def create_group():
    data = request.get_json()
    user_id = get_jwt_identity()
    name = data.get('name')
    description = data.get('description', '')
    if Group.query.filter_by(name=name).first():
        return jsonify({'error': 'Group name already exists'}), 400
    group = Group(name=name, description=description, created_by=user_id)
    db.session.add(group)
    db.session.commit()
    return group_schema.jsonify(group), 201

@group_bp.route('/groups', methods=['GET'])
@jwt_required()
def get_groups():
    groups = Group.query.all()
    return groups_schema.jsonify(groups), 200

@group_bp.route('/groups/<int:id>', methods=['GET'])
@jwt_required()
def get_group(id):
    group = Group.query.get_or_404(id)
    return group_schema.jsonify(group), 200

@group_bp.route('/groups/<int:id>', methods=['PUT'])
@jwt_required()
def update_group(id):
    group = Group.query.get_or_404(id)
    data = request.get_json()
    group.name = data.get('name', group.name)
    group.description = data.get('description', group.description)
    db.session.commit()
    return group_schema.jsonify(group), 200

@group_bp.route('/groups/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_group(id):
    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    return jsonify({'message': 'Group deleted'}), 200