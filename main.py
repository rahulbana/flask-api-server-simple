from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request
import os
app = Flask(__name__, static_url_path="")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")
print(HOST)
print(PORT)
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
	
	
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasksById(task_id):
    item = [task for task in tasks if task["id"] == task_id]
    return jsonify({'tasks': item})	


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host=HOST, port=PORT, debug=False)
    #app.run(host='0.0.0.0', port=5001, debug=False)
	
