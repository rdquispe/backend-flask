from models.models import User
from models.db_session import session
from flask import jsonify


class UserController:
    def __init__(self):
        pass

    @staticmethod
    def register_user(username, password, email, phone):
        user = User(username=username, email=email, phone=phone)
        user.hash_password(password=password)
        exist = session.query(User).filter(User.username == username).first()
        if exist:
            return jsonify({"message": "username exist"})
        else:
            session.add(user)
            session.commit()
            return jsonify({"username": user.username, "email": user.email, "phone": user.phone})
