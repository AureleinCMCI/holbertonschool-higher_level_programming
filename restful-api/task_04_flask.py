from flask import Flask, jsonify, request
'''
This module contains a simple HTTP server for GET requests
'''
app = Flask(__name__)

# Dictionnaire stockant les utilisateurs en mémoire
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    # Retourne la liste des utilisateurs sous format JSON
    return jsonify(list(users.keys()))  # Returning just the list of usernames

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)  # Vérifie si l'utilisateur existe dans le dictionnaire
    if user:
        return jsonify(user)  # Renvoie les informations de l'utilisateur sous forme de JSON
    else:
        return jsonify({"error": "User not found"}), 404  # Renvoie une erreur si l'utilisateur n'existe pas

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # Parse incoming JSON data

    username = data.get("username")
    if not username or username in users:
        return jsonify({"error": "Invalid or duplicate username"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added successfully", "user": users[username]}), 201

# Démarrer le serveur Flask sur le port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
