from flask import Flask, jsonify, request

app = Flask(__name__)

# Define some dummy data for users and posts
users = [
    {'id': 1, 'name': 'Steve ngandu', 'email': 'steve.ngandu@gmail.com'},
    {'id': 2, 'name': 'Gael kabuya',  'email': 'gael.kabuya@gmail.com'}
    {'id': 3, 'name': 'Larry kabala', 'email': 'larry.kabala@gmail.com'}
]

posts = [
    {'id': 1, 'title': 'Premier Post', 'content': 'Hello World!', 'user_id': 1},
    {'id': 2, 'title': 'Deuxième Post', 'content': 'DevOps est meilleur ', 'user_id': 2},
    {'id': 3, 'title': 'Troisième Post', 'content': 'Docker est intérressant', 'user_id': 1}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {'id': len(users) + 1, 'name': data['name'], 'email': data['email']}
    users.append(user)
    return jsonify(user), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {'id': len(posts) + 1, 'title': data['title'], 'content': data['content'], 'user_id': data['user_id']}
    posts.append(post)
    return jsonify(post), 201

if __name__ == '__main__':
    app.run(debug=True)