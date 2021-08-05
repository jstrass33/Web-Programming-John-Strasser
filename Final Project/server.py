from bottle import route, get, post, run, template, debug, request, response, redirect, static_file
import dataset
import json
from bottle import default_app
from dataset.types import MYSQL_LENGTH_TYPES

import json
import random
import string
import hashlib
import os
import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

# http://localhost:8080/


##################Note to JOhn - Left Off at Mail Trap Send Verification Email Part. Supposed to Send to User... but sending to mail trap instead? Odd

message=None
message2=None

def send_verification_email(username):
    #This finds the json file that contains the user information that the user just sumbmitted via the form
    print(username)
    user = get_user(username)
    print('Right before print user')
    print(user)
    if not user:
        #makes sure the user has a valid username file.
        print("failure to find user")
        return
    print(user)
    #takes the user's email from the user file and makes that the email variable
    email = user['email']
    #uses the get_token method to generate a long string of random characters that we can use to store as the verified token
    token = get_token()
    #Then stores that token in the user dictionsar and then writes that back to the user's file entry
    user['token'] = token
    save_user_data(username, user)
    print('user information with token has been saved')
    #sets the verify URL as your location host machine at the verify route with the token behind it ******** WILL NEED TO CHANGE WHEN ADDING TO PYTHON ANYWHERE ***********
    verify_url = f"http://localhost:8080/verify/{token}"

    # send_message(email, message)
    sender = "<app@example.com>"
    receiver = f"{username}<{email}>"

    text = f"""\
        Please verify your email by visiting this page in your browser. 
        
        {verify_url}

        Thanks! 

        The admins..
    """
    #Defines the HTML the your email message will have. Format accordingly
    html = f"""\
        <html>
        <body>
        <h4>Thank you for creating an account for John's Higher Views website!</h4>
        <br>
        <p>Please verify your email by clicking here.<br/></p>

        <p><a href="{verify_url}">{verify_url}</a><br/></p>

        <p>-Thank you!<br>John Strasser</p>
        </body>
        </html>
    """

    message = MIMEMultipart("alternative")
    #Adds to the message that will be sent - added a subject for my message
    message["Subject"] = "John's Higher Views - Please verify your email"
    message["From"] = sender
    message["To"] = receiver

    message.attach(MIMEText(text,"plain"))
    message.attach(MIMEText(html,"html"))
    #Sends the email using the mail trap could service. I updated the login with my personal credentials provided by mail trap.
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("68667044c825b5", "2635dda76b4d3c")
        server.sendmail(sender, receiver, message.as_string())

    print("sent mail at the end of mail function")
    return

def get_user(name):
    #tries to open a json file that was created during the signup proccess. This is stored in the directory of finalproject_data folder
    try:
        with open(f"finalproject_data/finalproject_user.{name}.json", "r") as f:
            #injests this json file and converts it to a python dictionary
            data = json.load(f)
            #makes sure its a dictionary
        assert type(data) is dict
        #returns the dictionary
        return data
    except:
        #if it does't exist, it returns nothing.
        return None

def get_token(k=32):
    #created a randome string of letters and digets that makes of the token. 32 caracters long. This serves as the token/session ID
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

def new_user_session_id():
    #to create a new session ID - this function returns the output of the new_token function.
    return get_token()

def get_session(request):

    print('inside of the get request function')

    def new_session():
        print('Inside the new session function')
        #calls the session_ID function which creates a random token of characters that will serve as the session id
        session_id = new_user_session_id()
        print("new session id = ", session_id)
        #creates a dictionary called session that includes the session ID and blank username for the time being
        session = {
            "session_id" : session_id,
            "username" : ''
        }
        return session
    #Looks at the the cookie called "session_id" to see what its value is
    session_id = request.get_cookie("session_id", default=None)
    if session_id == None:
        #If there is no session id, the program calls the new session function above to create a session id value
        session = new_session()
    else:
        #if there is a session_id value, the website reads that values and stores it as the session variable
        try:
            session = read(session_id)
        except: 
            session = new_session()
    print("loaded session = ", [session])
    #that session variable is then returned
    return session

def save_user_session(response, session):
    #calls the write function with takes the session id out of the current session dictionary and creates a file in the directory to save it.
    create_session_file(session['session_id'], session)
    print("saved session = ",[session])
    response.set_cookie("session_id", session['session_id'], path="/") #, secret='some-secret-key')

def create_session_file(key, data):
    #makes sure the data paremter is a dictionary
    assert type(data) is dict
    #creates a new file in the  finalproject_data folder where the user info is stored, as well.
    with open(f"finalproject_data/session.{key}.json", "w") as f:
        #formats the python dictionary to be a json format when creating it
        json.dump(data,f)
    return

def read(key):
    with open(f"finalproject_data/session.{key}.json", "r") as f:
        data = json.load(f)
    assert type(data) is dict
    return data

def save_user_data(name, data):
    assert type(data) is dict
    with open(f"finalproject_data/finalproject_user.{name}.json", "w") as f:
        json.dump(data,f)
    return

def hash_credentials(password):
    #The salt provides a 32 bit random number. This is then added to the password and hashed together. The purpose is to make the password hash signifigantly longer.
    #This longer hash makes it much harder for hackers to crack this hash.
    salt = os.urandom(32)
    #The key is the final hash with the password and hash mixed together
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    print(salt)
    print(key)
    return {
        #Needs to call the bytes to string function the take the salt and key data types which are bytes and converts them to strings
        'salt':bytes_to_str(salt), 
        'key' :bytes_to_str(key),
    }

def bytes_to_str(b):
    #This function takes parameter of a byte data type and converts it to a string and returns it
    s = str(codecs.encode(b,"hex"),"utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    #This function takes parameter of a string data type and converts it to a byte and returns it
    b = codecs.decode(bytes(s,"utf-8"),"hex")
    assert type(b) is bytes
    return b


@get("/signup")
def get_signup():
    error=''
    return template("signup", error=error)

@post("/signup")
def post_signup():
    #uses the get_session function to 
    session = get_session(request)
    print(session)
    username = request.forms.get('username')
    password = request.forms.get('password')
    password_again = request.forms.get('password_again')
    email = request.forms.get('email')
    if password != password_again:
        print('Passwords did not match')
        #if he passwords don't match, this creates and error variable that shows up on the sign-up sheet again once it redirects to it
        error="Your Passwords did Not Match - Try Again"
        save_user_session(response, session)
        #returns back to signup page with the appropriate error
        
        return template("signup", error=error)
    ########################################## Paused right here ***************************************************#####################################################
    #If the passwords to match, it calls the save user_data function which takes the username, password, email, and email verified data points and saves them.
    save_user_data(username, {
        'username':username,
        'credentials':hash_credentials(password),
        'email':email,
        'email_verified':False
    })
    
    send_verification_email(username)
    session['username'] = username
    #Saves the session information provided by the user
    save_user_session(response, session)
    return redirect('/')

@get("/login")
def get_login():
    #returns template for the login page.
    return template("login.tpl")



@post("/login")
def post_login():
    #inputs the request parameter into the get session function an returns the current sesstion for the user
    user_session = get_session(request)
    #Returns the input from the form from the name label in the HTML form
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = get_user(username)
    #Checks to make sure there was a username/file created
    if not user:
        #if not, directs it back to the signup page
        print("no such user")
        return redirect('/signup')
    
#THIS IS WHERE I PAUSED ***********************************************************************************************************88

    if 'credentials' not in user:
        print("credentials missing")
        return redirect('/signup')
    if not verify_password(password, user['credentials']):
        print('failed verification')
        return redirect('/')
    print("successful login")
    session['username'] = username
    save_session(response, session)
    return redirect('/')

@route("/")
def get_travelblog():

    return template("travelblog.tpl")

@route("/parklocations")
def get_locations():

    return template("parklocations.tpl")
@route("/parklocations2")
def get_locations():

    return template("parklocations2.tpl")
@route("/yosemite")
def get_banff():
    #Connects to the DB and pulls into from the banff table
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('yosemite')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    yosemite='yosemite'
    commentsnumber=len(items)
    items = reversed(items)

    

    return template("yosemite.tpl",  items=items, nationalpark=yosemite, commentsnumber=commentsnumber)

@route("/banff")
def get_banff():
    #Connects to the DB and pulls into from the banff table
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('banff')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    commentsnumber=len(items)
    items = reversed(items)
    banff='banff'
    

    

    return template("banff.tpl",  items=items, nationalpark=banff, commentsnumber=commentsnumber)

@route("/northcascades")
def get_northcascades():

    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('northcascades')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    northcascades='northcascades'
    commentsnumber=len(items)
    items = reversed(items)

    

    return template("northcascades.tpl",  items=items, nationalpark=northcascades, commentsnumber=commentsnumber)


@post("/comments")
def post_comments():
    nationalpark = request.forms.get('nationalpark')
    username = request.forms.get('username')
    comment = request.forms.get('comment')
    print(nationalpark)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
        nationalpark_table = nationalpark_db.get_table(nationalpark)
        nationalpark_table.insert({
            'username' : username.strip(),
            'comment' : comment.strip(),
            'date' : dt_string,
        })
        print('Succeeded in posting comment in DB')
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return

    return redirect ('/'+nationalpark)

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

    return redirect("/"+nationalpark)



@route('/static/<filename>')
def server_static(filename):

    return static_file(filename, root='./static')


if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
else:
    application = default_app()
