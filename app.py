from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['todoapp']
todos = db['todos']

@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        item_id = request.form.get('itemId')
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        if not item_id or not item_name or not item_description:
            return render_template('todo.html', error="All fields are required")
        
        # Check if item ID already exists
        if todos.find_one({'id': item_id}):
            return render_template('todo.html', error="Item ID already exists")
        
        # Insert into MongoDB
        todo_item = {
            'id': item_id,
            'name': item_name,
            'description': item_description
        }
        todos.insert_one(todo_item)
        
        return render_template('todo.html', success="Todo item added successfully!")
    except Exception as e:
        return render_template('todo.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
