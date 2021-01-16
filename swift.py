from bottle import route, run, template

@route('/')
def tasks():
    return template("tasks.tpl") 

run(host='localhost', port=8080, debug=True)