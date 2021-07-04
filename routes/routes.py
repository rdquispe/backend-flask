from flask import Flask, request
from flask_restful import Api
from controllers.user_controller import UserController
from controllers.hello_world_controller import HelloWorldController
from controllers.error_handler_controller import ErrorHandlerController
from controllers.hello_person_name_controller import HelloPersonNameController
from controllers.hello_person_last_name_controller import HelloPersonLastNameController

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)


@app.route('/user', methods=['POST'])
def register_user():
    username = request.json.get('user_name')
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    return UserController.register_user(username, password, email, phone)


@app.route('/hello_world', methods=['GET'])
def hello_world():
    return HelloWorldController.get_hello_word()


@app.route('/hello_person_last_name/<int:person_last_name>', methods=['GET'])
def hello_person_last_name(person_last_name):
    return HelloPersonLastNameController.post_person_last_name(person_last_name=person_last_name)


@app.route('/hello_person_name', methods=['POST'])
def hello_person_name():
    person_name = request.json.get('person_name', '')
    return HelloPersonNameController.post_person_name(person_name=person_name)


@app.errorhandler(404)
def not_found(error):
    return ErrorHandlerController.error_not_found(error=error)
