from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient
import uuid
import hashlib

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

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            role = request.form['role']
            
            # Read existing data
            with open('data.json', 'r') as file:
                data = json.load(file)
            
            # Add new entry
            data.append({"name": name, "role": role})
            
            # Write back to file
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)
            
            return render_template('success.html')
        except Exception as e:
            return render_template('form.html', error=str(e))
    
    return render_template('form.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        item_id = request.form.get('itemId')
        item_uuid = request.form.get('itemUuid')
        item_hash = request.form.get('itemHash')
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        if not all([item_id, item_uuid, item_hash, item_name, item_description]):
            return render_template('todo.html', error="All fields are required")
        
        # Check if item ID already exists
        if todos.find_one({'id': item_id}):
            return render_template('todo.html', error="Item ID already exists")
        
        # Insert into MongoDB
        todo_item = {
            'id': item_id,
            'uuid': item_uuid,
            'hash': item_hash,
            'name': item_name,
            'description': item_description
        }
        todos.insert_one(todo_item)
        
        return render_template('todo.html', success="Todo item added successfully!")
    except Exception as e:
        return render_template('todo.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
