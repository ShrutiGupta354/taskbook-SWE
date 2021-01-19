# SWIFT Taskbook
# Web Application for Task Management 

# web transaction objects
from bottle import request, response

# HTML request types
from bottle import route, get, put, post, delete

# web page template processor
from bottle import template 

# development server
from bottle import run 

# ---------------------------
# web application routes
# ---------------------------

@route('/')
@route('/tasks')
def tasks():
    return template("tasks.tpl") 

@route('/login')
def login():
    return template("login.tpl") 

@route('/register')
def login():
    return template("register.tpl") 

# ---------------------------
# task REST api 
# ---------------------------

import json
import dataset
import time

taskbook_db = dataset.connect('sqlite:///taskbook.db')  

@get('/api/tasks')
def get_tasks():
    'return a list of tasks sorted by submit/modify time'
    print("Getting tasks")
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    task_table = taskbook_db.get_table('task')
    tasks = [dict(x) for x in task_table.find(order_by='time')]
    return { "tasks": tasks }

@post('/api/tasks')
def create_task():
    'create a new task in the database'
    try:
        data = request.json
        assert type(data['description']) is str
        assert len(data['description'].strip()) > 0
        assert type(data['list']) is str
        assert data['list'] in ["today","tomorrow"]
    except:
        response.status = 400
        return
    try:
        task_table = taskbook_db.get_table('task')
        task_table.insert({
            "time": time.time(),
            "description":data['description'].strip(),
            "list":data['list'],
            "completed":False
        })
        print("creating ", {
            "time": time.time(),
            "description":data['description'].strip(),
            "list":data['list'],
            "completed":False
        })
    except:
        response.status = 409
        return
    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'success': True})

@put('/api/tasks')
def update_task():
    'update properties of an existing task in the database'
    try:
        data = request.json
        assert type(data['id']) is int
    except:
        response.status = 400
        return
    if 'list' in data: 
        data['time'] = time.time()
    try:
        task_table = taskbook_db.get_table('task')
        task_table.update(row=data, keys=['id'])
        print("updating ",data)
    except:
        response.status = 409
    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'success': True})

@delete('/api/tasks')
def delete_task():
    'delete an existing task in the database'
    try:
        data = request.json
        assert type(data['id']) is int
    except:
        response.status = 400
        return
    try:
        task_table = taskbook_db.get_table('task')
        task_table.delete(id=data['id'])
        print("deleting ",data)
    except:
        response.status = 409
    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'success': True})

if __name__ == "__main__":

    run(host='localhost', port=8080, debug=True)