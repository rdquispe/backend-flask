from flask_restful import abort
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

        session.add(user)
        session.commit()

        exist = session.query(User).filter(User.username == username).first()
        if not exist:
            abort(404, message="User {} doesn't exist".format(username))
        return jsonify({'message': 'Hello World'})
