from flask import request
from flask_restful import Resource
from app.models.user import User

class UserListResource(Resource):
    def get(self):
        """Get all users"""
        users = User.find_all()
        return {'data': users}, 200
    
    def post(self):
        """Create a new user"""
        data = request.get_json()
        
        # Input validation
        if not data or not data.get('name') or not data.get('email'):
            return {'message': 'Missing required fields (name, email)'}, 400
        
        try:
            user = User.create(data['name'], data['email'])
            return {'data': user.to_dict(), 'message': 'User created successfully'}, 201
        except Exception as e:
            return {'message': str(e)}, 500

class UserResource(Resource):
    def get(self, user_id):
        """Get a single user by ID"""
        user = User.find_by_id(user_id)
        if user:
            return {'data': user.to_dict()}, 200
        return {'message': 'User not found'}, 404
    
    def put(self, user_id):
        """Update a user"""
        data = request.get_json()
        user = User.update(user_id, data)
        
        if user:
            return {'data': user.to_dict(), 'message': 'User updated successfully'}, 200
        return {'message': 'User not found'}, 404
    
    def delete(self, user_id):
        """Delete a user"""
        success = User.delete(user_id)
        
        if success:
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404