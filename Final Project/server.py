from bottle import route, get, post, run, template, debug, request, response, redirect, static_file
import dataset
import json
from bottle import default_app
from dataset.types import MYSQL_LENGTH_TYPES

# http://localhost:8080/




message=None
message2=None

@route("/")
def get_todo_list():
    todo_list_db = dataset.connect('sqlite:///todo_list.db')
    todo_table = todo_list_db.get_table('todo')
    items = todo_table.find()
    items = [ dict(x) for x in list(items) ]

    return template("todo_list", items=items)

@route("/comments")
def get_comments():
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('yosemite')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    yosemite='yosemite'
    commentsnumber=len(items)

    return template("comments", items=items, nationalpark=yosemite, commentsnumber=commentsnumber)

@post("/comments")
def post_comments():
    nationalpark = request.forms.get('nationalpark')
    username = request.forms.get('username')
    comment = request.forms.get('comment')
    print(nationalpark)
    try:
        nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
        nationalpark_table = nationalpark_db.get_table(nationalpark)
        nationalpark_table.insert({
            'username' : username.strip(),
            'comment' : comment.strip()
        })
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return

    return redirect ('/comments')

@route("/delete/<nationalpark>/<id>")
def get_delete(nationalpark,id):
    id = int(id)

    try:
        nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
        nationalpark_table = nationalpark_db.get_table(nationalpark)
        print(f"We need to delete id# {id}...")
        nationalpark_table.delete(id=id)
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return

    return redirect("/comments")


@route("/midterm")
def get_midterm():
    
    global message
    global message2
    hobby_list_db = dataset.connect('sqlite:///hobby_list.db')
    hobby_table = hobby_list_db.get_table('hobby')
    items = hobby_table.find()
    items = [ dict(x) for x in list(items) ]
    tpl = template("midterm.tpl", items=items, message=message, message2=message2)
    message=None
    message2=None
    return tpl

@post("/midterm")
def post_midterm():
    global message
    message = "A hobby was added"
    
    hobby = request.forms.get('newhobby')
    years = request.forms.get('years')
    print(hobby)
    print(years)
    try:
        hobby_list_db = dataset.connect('sqlite:///hobby_list.db')
        hobby_table = hobby_list_db.get_table('hobby')
        hobby_table.insert({
            'hobby' : hobby.strip(),
            'years' : years.strip()
        })
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return

    
    
    return redirect("/midterm")

@route("/delete_hobby/<id>")
def get_delete(id):
    global message2
    message2 = "A hobby was deleted"
    id = int(id)
    try:
        hobby_list_db = dataset.connect('sqlite:///hobby_list.db')
        hobby_table = hobby_list_db.get_table('hobby')
        print(f"We need to delete id# {id}...")
        hobby_table.delete(id=id)
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    
   

    return redirect("/midterm")

@route('/static/<filename>')
def server_static(filename):

    return static_file(filename, root='./static')

@route("/data")
def get_data():
    pets = [
    {
        "name": "Dorothy",
        "kind": "dog",
    },
    {
        "name": "Squeakers",
        "kind": "guinea pig",
    },
    {
        "name": "Sandy",
        "kind": "cat",
    }
    ]
    
    response.content_type = 'application/json'
    return json.dumps({"pets":pets})

@route("/show")
def get_show():
    return template("show")

@route('/counter')
def get_counter():
    count = int(request.get_cookie("count", default='0', secret="Elephant12"))
    count = count + 1
    response.set_cookie("count", str(count), secret="Elephant12")
    return template("counter", count=count)

@route("/delete/<id>")
def get_delete(id):
    id = int(id)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        print(f"We need to delete id# {id}...")
        todo_table.delete(id=id)
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return template("deleted", id=id)

@get("/insert")
def get_insert():
    return template("insert")

@post("/insert")
def post_insert():
    task = request.forms.get('task')
    print("task=", task)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        todo_table.insert({
            'task' : task.strip(),
            'done' : 0
        })
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return template("inserted")

@get("/edit/<id>")
def get_edit(id):
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        items = list(todo_table.find(id=id))
        if len(items) != 1:
            response.status="404 Not Found:"+str(id)
            return
        items = [ dict(x) for x in items ]
        print(items)
        print(items[0])
    except Exception as e:
        print(e)
        response.status="409 Bad Request:"+str(e)
        return

    return template("edit", item=items[0])  # put something here

@post("/edit")
def post_edit():
    id = request.forms.get('id')
    id = int(id)
    task = request.forms.get('task')
    print("task=", task)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        todo_table.update({
            'id' : id,
            'task' : task.strip(),
        }, ['id'])
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')

if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
else:
    application = default_app()
