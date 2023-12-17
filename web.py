from flask import Flask, jsonify, request
from rest.service import Service

app = Flask(__name__)
service = Service()

@app.route('/users', methods=['GET'])
def get_all_users():
    users = service.get_all_users()
    return jsonify(users)

@app.route('/users/<name>', methods=['GET'])
def get_user_by_name(name):
    user_email = service.get_user_by_name(name)
    if user_email is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'name': name, 'email': user_email})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    service.create(name, email)
    return jsonify({'message': 'User created successfully'}), 201


if __name__ == '__main__':
    app.run()

