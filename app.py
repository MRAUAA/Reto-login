from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
users_collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users_collection.find_one({'username': username, 'password': password}):
            return 'Login successful'
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    