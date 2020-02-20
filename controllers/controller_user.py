from flask_restful import abort
from models.models import User
from models.db_session import session
from flask import jsonify


class ControllerUser:
    def __init__(self):
        pass

    @staticmethod
    def register_user(user_name, password):
        user = User(username=user_name)
        user.hash_password(password=password)
        session.add(user)
        session.commit()

        reged_user = session.query(User).filter(User.username == user_name).first()
        if not reged_user:
            abort(404, message="User {} doesn't exist".format(user_name))
        return jsonify({'message': 'Hello World'})
