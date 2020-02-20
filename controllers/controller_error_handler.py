from flask import jsonify, make_response


class ControllerErrorHandler:

    def __init__(self):
        pass

    @staticmethod
    def error_not_found(error):
        return make_response(jsonify({'error': 'not found', 'description': error}), 404)
