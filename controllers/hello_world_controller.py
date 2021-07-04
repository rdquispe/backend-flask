from flask import jsonify


class HelloWorldController:

    def __init__(self):
        pass

    @staticmethod
    def get_hello_word():
        return jsonify({'message': 'Hello World'})
