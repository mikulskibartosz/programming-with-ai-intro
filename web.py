from flask import Flask, jsonify, request
from rest.db_service import DbService

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all_users():
    service = DbService()
    users = service.get_all_users()
    service.close()
    return jsonify(users)

@app.route('/users/<name>', methods=['GET'])
def get_user_by_name(name):
    service = DbService()
    user_email = service.get_user_by_name(name)
    service.close()
    if user_email is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'name': name, 'email': user_email})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    service = DbService()
    service.create(name, email)
    service.close()
    return jsonify({'message': 'User created successfully'}), 201


@app.route('/users', methods=['PUT'])
def update_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name is None or email is None:
        return jsonify({'error': 'Missing name or email'}), 400
    try:
        service = DbService()
        service.update_email(name, email)
        service.close()
        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404
    

@app.route('/users/<name>', methods=['DELETE'])
def delete_user(name):
    try:
        service = DbService()
        service.delete_user_by_name(name)
        service.close()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    app.run()

