from datetime import datetime
import uuid

# Simple in-memory database to store users
users_db = {}

class User:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }
    
    @classmethod
    def create(cls, name, email):
        user = cls(name, email)
        users_db[user.id] = user
        return user
    
    @classmethod
    def find_all(cls):
        return [user.to_dict() for user in users_db.values()]
    
    @classmethod
    def find_by_id(cls, user_id):
        return users_db.get(user_id)
    
    @classmethod
    def update(cls, user_id, update_data):
        user = cls.find_by_id(user_id)
        if user:
            for key, value in update_data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            return user
        return None
    
    @classmethod
    def delete(cls, user_id):
        if user_id in users_db:
            del users_db[user_id]
            return True
        return False