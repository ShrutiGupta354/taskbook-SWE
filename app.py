# SWIFT Taskbook
# Web Application for Task Management 

# flask web objects
from auth import auth
from flask import Flask
from flask import render_template
from flask import request, session, flash
import dataset

taskbook_db = dataset.connect('sqlite:///taskbook.db')

# the base Flask object
app = Flask(__name__)
# for cookies and sesion encryption
app.config['SECRET_KEY'] = 'walsh-swe'

# ---------------------------
# web application routes
# ---------------------------

@app.get('/')
@app.get('/home')
def homepage():
    if session.get('user_authenticated'):
        flash('Log out first to log back in.')
        return render_template('tasks.html')
    return render_template("homepage.html")

@app.get('/calendar')
def calendar():
    if session.get('user_authenticated'):
        return render_template("calendar.html", user=session['user_email'])
    flash('You need to be logged in first', category='error')
    return render_template("login.html")
    
@app.get('/tasks')
def tasks():
    if session.get('user_authenticated'):
        return render_template("tasks.html", user=session['user_email'])
    flash('You need to be logged in first', category='error')
    return render_template("login.html")

@app.get('/weekly')
def weekly():
    if session.get('user_authenticated'):
        return render_template("weekly.html", user=session['user_email'])
    flash('You need to be logged in first', category='error')
    return render_template("login.html")

@app.get('/tasks-w3')
def tasks_w3():
    if session.get('user_authenticated'):
        return render_template("tasks-w3.html", user=session['user_email'])
    flash('You need to be logged in first', category='error')
    return render_template("login.html")

#--------------------
# For authentication
#-------------------
# we need this so that we can "import" login/logout/signup functions from auth.py
app.register_blueprint(auth, url_prefix='/')

# ---------------------------
# task REST api 
# ---------------------------

@app.get('/api/tasks')
def get_tasks():
    'return a list of tasks sorted by submit/modify time'
    task_table = taskbook_db.get_table('task')
    tasks = [dict(x) for x in task_table.find(order_by='date')]
    return { "tasks": tasks }

@app.post('/api/tasks',)
def create_task():
    'create a new task in the database'
    try:
        data = request.get_json()
        for key in data.keys():
            assert key in ["description", "date", "time"], f"Illegal key '{key}'"
        assert type(data['description']) is str, "Description is not a string."
        assert len(data['description'].strip()) > 0, "Description is length zero."
    except Exception as e:
        print(400, str(e))
        return ("400 Bad Request:"+str(e), 400)
    try:
        task_table = taskbook_db.get_table('task')
        task_table.insert({
            "email":session['user_email'],
            "description":data['description'].strip(),
            "date":data['date'],
            "time":data['time'],
            "completed":False
        })
    except Exception as e:
        print(409, str(e))
        return ("409 Bad Request:"+str(e), 409)
    # return Success
    return {'status':200, 'success': True}

@app.put('/api/tasks')
def update_task():
    'update properties of an existing task in the database'
    try:
        data = request.get_json()
        for key in data.keys():
            assert key in ["id","description","completed"], f"Illegal key '{key}'"
        assert type(data['id']) is int, f"id '{id}' is not int"
        if "description" in data:
            assert type(data['description']) is str, "Description is not a string."
            assert len(data['description'].strip()) > 0, "Description is length zero."
        if "completed" in data:
            assert type(data['completed']) is bool, "Completed is not a bool."
    except Exception as e:
        print(400, str(e))
        return ("400 Bad Request:"+str(e), 400)
    if 'date' in data: 
        data['date'] = data['date']
    try:
        task_table = taskbook_db.get_table('task')
        task_table.update(row=data, keys=['id'])
    except Exception as e:
        print(409, str(e))
        return ("409 Bad Request:"+str(e), 409)
    # return Success
    return {'status':200, 'success': True}

@app.delete('/api/tasks')
def delete_task():
    'delete an existing task in the database'
    try:
        data = request.get_json()
        assert type(data['id']) is int, f"id '{id}' is not int"
    except Exception as e:
        print(400, str(e))
        return ("400 Bad Request:"+str(e), 400)
    try:
        task_table = taskbook_db.get_table('task')
        task_table.delete(id=data['id'])
    except Exception as e:
        print(409, str(e))
        return ("409 Bad Request:"+str(e), 409)
    # return Success
    return {'status':200, 'success': True}
