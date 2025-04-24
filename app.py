from flask import Flask, jsonify, render_template, request, redirect, url_for
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
