from flask import Flask, jsonify
from rest.service import Service

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all_users():
    service = Service()
    users = service.get_all_users()
    return jsonify(users)

if __name__ == '__main__':
    app.run()

