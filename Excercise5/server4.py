from bottle import debug, route, run, template, debug, post, get, request,response, redirect
import dataset


#http://localhost:8068/foobar


@route("/")
def get_todo_list():
    
    todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
    todo_table = todo_list_db.get_table('todo')

    items = todo_table.find()
    items = [ dict(x) for x in list(items) ]
    #data= {
       # 'items':[
        #    {'task':'Figure out how to write Python with database','done': 0},
         #   {'task':'Practice the syntax for this','done': 0},
        #    {'task':'Continue to work on this stupid database stuff','done': 0},
       # ]
  #  }



    
    return template("todo_list.tpl", data=items)

@route("/delete/<id>")
def get_delete(id):
    id = int(id)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
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
        todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
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
        todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
        todo_table = todo_list_db.get_table('todo')
        items = list(todo_table.find(id=id))
        #The length of  ID is checked because if it comes back as 0, then you didnt get an ID and you can't update it. Searching for 1. If not one, you didnt find the ID. Not there.
        if len(items) !=1:

            response.status="404 Not Found:"+str(e)
            return
    
        items = [ dict(x) for x in list(items) ]
    
    #Exception - creates exception object that is general. Works all kinds of broad errors and treats them as e and then records them.
    except Exception as e:
        print(e)
        response.status="409 Bad Request:"+str(e)
        return
        print(items)
    return template("edit", item=items[0] )


@post("/edit")
def post_edit():
    id = request.forms.get('id')
    id = int(id)
    task = request.forms.get('task')
    print("task=", task)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list_john.db')
        todo_table = todo_list_db.get_table('todo')
        todo_table.update({ 
            'id' : id,
            'task' : task.strip(), 
        }, ['id'])
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')

@get("/counter")
def post_edit():
    #grabs a cooker from the web server
    #count=int(request.cookies.get("count", 0)  )
    #This gets the cookie and then makes sure its signed using the random text. Helps validate. If not, any user can use develpment tools and edit the cookie. #security
    count=int(request.get_cookie("count", default='0', secret="Elephant12")  )
    count= count + 1
    #sends the cookie back to the web server after it incremented
    response.set_cookie("count", str(count), secret="Elephant12")

    #many sites make you accept that they take cookies. If your browser collects that info about you, its an invasion of privacy. Thats where the targeted adds come from.
    #Why you go to a site, and then see a google add for it. The browser collects that. Google can do it across platforms and collect info about you.
    #Why Apple is having a war with Facebook, apple trying to sell privacy where that is where Facebook makes revenue from the targeted adds.

    return template("counter", count=count)

#run = fake web server that is used to run in dev. DONT USE IN PROD SERVER ENVIRONMENT
debug(True)
run (host="localhost", port=8098, reloader=True)
#WSGI = protocol allows the top end to talk to the bottom end.
#NgX = other webserver

#fsdff