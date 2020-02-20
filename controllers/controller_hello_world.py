from flask import jsonify


class ControllerHelloWorld:

    def __init__(self):
        pass

    @staticmethod
    def get_hello_word():
        return jsonify({'message': 'Hello World'})
