from flask import Flask, request
from flask_restful import Api
from controllers.controller_user import ControllerUser
from controllers.controller_hello_world import ControllerHelloWorld
from controllers.controller_error_handler import ControllerErrorHandler
from controllers.controller_hello_person_name import ControllerHelloPersonName
from controllers.controller_hello_person_last_name import ControllerHelloPersonLastName

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)


@app.route('/user', methods=['POST'])
def register_user():
    username = request.json.get('user_name')
    password = request.json.get('password')
    return ControllerUser.register_user(username, password)


@app.route('/hello_world', methods=['GET'])
def hello_world():
    return ControllerHelloWorld.get_hello_word()


@app.route('/hello_person_last_name/<int:person_last_name>', methods=['GET'])
def hello_person_last_name(person_last_name):
    return ControllerHelloPersonLastName.post_person_last_name(person_last_name=person_last_name)


@app.route('/hello_person_name', methods=['POST'])
def hello_person_name():
    person_name = request.json.get('person_name', '')
    return ControllerHelloPersonName.post_person_name(person_name=person_name)


@app.errorhandler(404)
def not_found(error):
    return ControllerErrorHandler.error_not_found(error=error)
