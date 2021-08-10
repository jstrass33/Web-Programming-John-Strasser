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
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

import base64

# http://localhost:8080/


##################Note to JOhn - Left Off at Mail Trap Send Verification Email Part. Supposed to Send to User... but sending to mail trap instead? Odd



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
    sender = "John's Higher Views<app@example.com>"
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

    print("About to print email....")
    print(email_bytes)
    print(emailp)
    message.attach(MIMEText(text,"plain"))
    message.attach(MIMEText(html,"html"))
    context = ssl.create_default_context()
    #Sends the email using the mail trap could service. I updated the login with my personal credentials provided by mail trap.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(#Gmail account, #####need to add google creds - removed for security concerns)
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
    return

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
    #Ensures the data is a dictionary
    assert type(data) is dict
    #opens the the user file and saves any changes in json format.
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
    print("Printing key inside of hash credentials below")
    print(bytes_to_str(key))
    #Needs to call the bytes to string function the take the salt and key data types which are bytes and converts them to strings
    return {
        
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

def verify_password(password, credentials):
    #Takes the input of the password that was provided during the login session and the credentials pulled from the user's json file to compare them
    #First it convers the credentials salt and key to bytes.
    salt = str_to_bytes(credentials['salt'])
    key  = str_to_bytes(credentials['key'])
    print(salt)
    print(key)
    #Then it runs the hashing algorthim the create a hash of the password the user provided combined with the salt from the original credential file
    new_key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    print('New key below')
    print(new_key)
    #It returns true or false depending if the keys match
    return new_key == key

def send_reset_email(username):
    global email_john
    global emailp
    #Checks the user file for the username provided by the user.
    user = get_user(username)
    if not user:
        #if the user is not found, it returns without doing anything further.
        print("failure to find user")
        
        return
    print(user)
    #From the user data/file, it pulls the email that it stored
    email = user['email']
    #It creates another token to use for the URL
    token = get_token()
    #It stores the token in the user data pulled
    user['reset_token'] = token
    #It then saves that token back into the user's data file.
    save_user_data(username, user)
    print('user information with reset token has been saved')

    reset_url = f"http://localhost:8080/reset/{username}/{token}"

    # send_message(email, message)
    sender = "John's Higher Views<app@example.com>"
    receiver = f"{username}<{email}>"

    text = f"""\
        John's Higher Views

        Please reset your password by visiting this page in your browser. 
        
        {reset_url}

        Thanks! 

        The admins..
    """

    html = f"""\
        <html>
        <body>
        <h3>John's Higher Views</h3>
        <p>Please reset your password by visiting this page in your browser. .<br/></p>

        <p><a href="{reset_url}">{reset_url}</a><br/></p>

        <p>-Thank you!<br>John Strasser</p>
        </body>
        </html>
    """
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "John's Higher Views - Password reset request"
    message["From"] = sender
    message["To"] = receiver

    message.attach(MIMEText(text,"plain"))
    message.attach(MIMEText(html,"html"))

    context = ssl.create_default_context()
    #Sends the email using the mail trap could service. I updated the login with my personal credentials provided by mail trap.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_john, emailp)
        server.sendmail(sender, receiver, message.as_string())

    return
def connect_to_db(nationalpark):
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table(nationalpark)
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    
    #Countings the number of comments
    commentsnumber=len(items)
    #Inverts the dictionary list so the most recent comments show up first
    items = reversed(items)

    return commentsnumber,items

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
    print('Made it to the end of the post signup function.')
    return redirect('/')

@get("/login")
def get_login():
    error=""
    #returns template for the login page.
    return template("login.tpl", error=error)



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
        error = "Username does not exist."
        return template('login', error=error)
    
#THIS IS WHERE I PAUSED ***********************************************************************************************************88

    if 'credentials' not in user:
        error = "Password does not exist.Try again."
        return template('login', error=error)
    #It checks to see if the password provided by the user matches the hash in the original credentials. If a value is returned, it was the same.
    if not verify_password(password, user['credentials']):
        print('failed verification')
        error = "Failed verification."
        return template('login', error=error)
    print("successful login")
    #If the passwords do match, the session is then updated with the username that is being logged in.
    user_session['username'] = username
    #This updated session info is then saved in the below function.
    save_user_session(response, user_session)
    return redirect('/')

@route("/")
def get_travelblog():
    #Needed to get the variable from the session for who was logged in.
    session = get_session(request)
    user=session['username'] 

    return template("travelblog.tpl", user=user)

@route("/forgot")
def get_travelblog():
    
    return template("forgot.tpl")

@post("/forgot")
def post_signup():
    session = get_session(request)
    #Returns the value from the form from the text fiel named "username".
    username = request.forms.get('username')
    #Gets the user json file from the username input from the form
    user = get_user(username)
    #Checks to see if the email in the json file has been verified
    if user['email_verified']:
        send_reset_email(username)
        return redirect('/login')
    else:
        error="You do not have a verified email or valid username."
        return redirect('/signup')

@route("/parklocations")
def get_locations():
    #Takes in the user from the session data and renders the park location template.
    session = get_session(request)
    user=session['username'] 
    return template("parklocations.tpl", user=user)

@route("/yosemite")
def get_banff():
    #Connects to the DB and pulls into from the banff table
    #I created seperate tables in the database for each album so the comments would be seperate
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('yosemite')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    yosemite='yosemite'
    #Counts the number of comments
    commentsnumber=len(items)
    #Inverts the dictionary list so the most recent comments show up first
    items = reversed(items)

    session = get_session(request)
    user=session['username'] 

    error=''

    return template("yosemite.tpl",  items=items, nationalpark=yosemite, commentsnumber=commentsnumber, user=user, error=error)

@route("/banff")
def get_banff():
    #Connects to the DB and pulls into from the banff table
    #I created seperate tables in the database for each album so the comments would be seperate
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('banff')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    #Counting the number of comments
    commentsnumber=len(items)
    #Inverts the dictionary list so the most recent comments show up first
    items = reversed(items)
    banff='banff'
    
    session = get_session(request)
    user=session['username'] 
    

    return template("banff.tpl",  items=items, nationalpark=banff, commentsnumber=commentsnumber, user=user)

@route("/northcascades")
def get_northcascades():
    #Connects to the DB and pulls into from the banff table
    #I created seperate tables in the database for each album so the comments would be seperate
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('northcascades')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    northcascades='northcascades'
    #Countings the number of comments
    commentsnumber=len(items)
    #Inverts the dictionary list so the most recent comments show up first
    items = reversed(items)

    session = get_session(request)
    user=session['username'] 

    return template("northcascades.tpl",  items=items, nationalpark=northcascades, commentsnumber=commentsnumber, user=user)

@route("/olympic")
def get_northcascades():
    #Connects to the DB and pulls into from the banff table
    #I created seperate tables in the database for each album so the comments would be seperate
    nationalpark_db = dataset.connect('sqlite:///nationalpark.db')
    nationalpark_table = nationalpark_db.get_table('olympic')
    items = nationalpark_table.find()
    items = [ dict(x) for x in list(items) ]
    olympic='olympic'
    #Countings the number of comments
    commentsnumber=len(items)
    #Inverts the dictionary list so the most recent comments show up first
    items = reversed(items)

    session = get_session(request)
    user=session['username'] 

    return template("olympic.tpl",  items=items, nationalpark=olympic, commentsnumber=commentsnumber, user=user)

@get("/verify/<token>")
#THis route takes the URL sent by the verify email route and when clicked it initiates the below function. The token is the variable assigned to the end of that URL
def get_verify(token):
    #Gets the session info
    session = get_session(request)
    #Gets the username from the session info
    username = session['username']
    #Gets the user's json file
    user = get_user(username)
    if user == None:
        error = "You have to be logged in while verifying your email."
        return template("login", error=error)
    print(token)
    print(user)
    #This then checks to see if the token that was stored initially in the user's json file matches what was recieved in the route.
    if token == user['token']:
        #If it matches, it then sets the email verified element to being true and saves the users file.
        user['email_verified'] = True
        save_user_data(username, user)
        return redirect("/")


@get("/reset/<username>/<reset_token>")
#Route takes in the username and reset token variables from the URL 
def get_reset(username, reset_token):
    session = get_session(request)
    #Uses the get token function to create a token which is used for a csrf token. This makes the form more secure by helping prevent CSRF attacks by making it impossible for an attacker to construct a fully valid HTTP
    session['csrf_token'] = get_token()
    #Gets the user's data file
    user = get_user(username)
    print(reset_token)
    print(user)
    #Checks to make sure the reset token is the one in the user's data file.
    if reset_token == user['reset_token']:
        #If the token does match, it will will save the csrf token to the session and then pass the data to the template.
        save_user_session(response, session)
        return template("reset", username=username, reset_token=reset_token, csrf_token=session['csrf_token'])
    return redirect('/')

@post("/reset/<username>/<reset_token>")
#Route takes in the username and reset token variables from the URL 
def post_reset(username, reset_token):

    session = get_session(request)
    #Checks to see a csrf token is in the session 
    if 'csrf_token' not in session:
        error="The CRSF token was not in the current secction"
        redirect('/', error=error)
    # Compares the csrf token that was created in the get part of the proccess matches what was put into the session in the previous step
    if request.forms.get('csrf_token') != session['csrf_token']:
        #If it does not match, it redirects to the root route
        redirect('/')
    #This resets the crsf token. Bascially clearing it for future use.
    session['csrf_token'] = None
    #Gets the user's json/data file
    user = get_user(username)
    print(reset_token)
    print(user)
    #Compares the tokens from the URL to the token that was stored in the user's data file during the first part of the reset proccess. Basically a security featuer to make sure they match.
    if reset_token != user['reset_token']:
        return redirect('/')
    #Resets the rest token in the user data file. Not saved yet.
    user['reset_token'] = None
    # gets new password from form
    password = request.forms.get('password')
    #Gets the new password again from the second input entry
    password_again = request.forms.get('password_again')
    #Compares the two passwords to make sure they match
    print(password + ' ' + password_again)
    if password != password_again:
        #Saves the user session with the data changed
        save_user_session(response, session)
        return redirect('/') 
    beforecredchange=user['credentials']
    print('Before new hash') 
    print(beforecredchange) 
    #Calls the generate credentials method with the new password provided and then stores this in the user credentials variable.
    newcredentials= hash_credentials(password)
    print('new creds below')
    print(newcredentials)
    user['credentials'] = newcredentials
    aftercredchange=user['credentials']
    print('After Creential change')
    print(aftercredchange)  
    #Then saves that new password in the users json/data file.
    save_user_data(username, user)

    #Finally, redirects to the login page to allow the user to login
    return redirect('/login')


@get("/logout")
def get_logout():
    #Gets the current session info
    session = get_session(request)
    #Sets the username session info to being none
    session['username'] = ''
    #Then saves this session info back and returns the user to the main route.
    save_user_session(response, session)
    return redirect('/')

@post("/comments")
def post_comments():
    #Gets the nationation park variable from the hidden form input on the template
    nationalpark = request.forms.get('nationalpark')
    session = get_session(request)
    username=session['username'] 
    #Makes sure that only a user logged in can make a comment
    if username == '':
        print('You muse be signed in to make a comment.')
        
        return redirect('/'+nationalpark)
    #Grabs the comment from the text box
    comment = request.forms.get('comment')
    print(nationalpark)
    #Grabs the current date
    now = datetime.now()
    #Formats the current date
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    try:
        #connects to the DB and adds the comment entry to it.
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
    #Takes the nationalpark and ID variable from the template
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

@route("/drawing")
def get_drawing():


    return template("drawing")


if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
else:
    application = default_app()
