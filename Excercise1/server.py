from bottle import route, run, template


#http://localhost:8068/foobar
@route("/")
def get_index():

    return "Hello!"


#run = fake web server that is used to run in dev. DONT USE IN PROD SERVER ENVIRONMENT
run (host="localhost", port=8097)
#WSGI = protocol allows the top end to talk to the bottom end.
#NgX = other webserver