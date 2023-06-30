from flask import Flask, jsonify, request

app = Flask(__name__)

# Define some dummy data for users and posts
users = [
    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'id': 2, 'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
]

posts = [
    {'id': 1, 'title': 'First Post', 'content': 'Hello World!', 'user_id': 1},
    {'id': 2, 'title': 'Second Post', 'content': 'Flask is awesome!', 'user_id': 2},
    {'id': 3, 'title': 'Third Post', 'content': 'RESTful APIs are cool!', 'user_id': 1}
]

# Define a route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Define a route to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Define a route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {'id': len(users) + 1, 'name': data['name'], 'email': data['email']}
    users.append(user)
    return jsonify(user), 201

# Define a route to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Define a route to get a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404

# Define a route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {'id': len(posts) + 1, 'title': data['title'], 'content': data['content'], 'user_id': data['user_id']}
    posts.append(post)
    return jsonify(post), 201

if __name__ == '__main__':
    app.run(debug=True)