from flask import jsonify


class HelloPersonNameController:

    def __init__(self):
        pass

    @staticmethod
    def post_person_name(person_name):
        return jsonify({'status': 'ok', 'person_name': person_name})
