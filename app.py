from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
<<<<<<< HEAD
def add_item():
    item = request.json
    todos.append(todo)
    return jsonify(item), 201
=======
def add_todo():
    todo = request.json

    # add item only if it is not already present
    if todo in todos:
        return jsonify({'error': 'Item already exists'}), 400
    else:
        todos.append(todo)
        return jsonify(todo), 201
>>>>>>> origin/bob

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = request.json
    todos[todo_id] = todo
    return jsonify(todo), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = todos.pop(todo_id)
    return jsonify(todo), 200

if __name__ == '__main__':
    app.run(debug=True)