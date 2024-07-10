import json
import uuid


class User:
    """The user Class"""

    def __init__(self, username, email):
        """initilization"""
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email

    def to_dict(self):
        """ Serialization"""
        return {"id": self.id, "username": self.username, "email": self.email}

    @staticmethod
    def from_dict(data):
        """Deserialization"""
        user = User(data["username"], data["email"])
        user.id = data["id"]
        return user
