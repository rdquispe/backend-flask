from flask import jsonify


class HelloPersonLastNameController:

    def __init__(self):
        pass

    @staticmethod
    def post_person_last_name(person_last_name):
        return jsonify({'status': 'ok', 'person_last_name': person_last_name})
