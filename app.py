
from flask import Flask,request,redirect,render_template,session
from pymongo import Connection,MongoClient

################################ mongo stuff ############################
'''client = MongoClient()
db = client['portas-troiae']
#collection = db['user-info']

def add(username,password):
    #adds to the database
    db.users.insert( {'name': username, 'password': password} )

def check(username, password):
    #makes sure the username and password are valid
    if db.users.find( {'name': name} ) != null: #not sure how to do this?!
        #this user already exists
        return False
    if len(password) < 4:
        #password is too short
        return False
    else:
        return True



'''

################################ webapp stuff ###########################

app=Flask(__name__)

@app.route("/")
def base():
    """success = 0
    logging = 0
    if 'n' not in session:
        session['n']= "save in session"
        return "session set"
    else:
        return sessions['n']"""
    return render_template("testLogin.html", success = 0, logging = 0)

@app.route("/logging", methods=['POST'])
def index():
    if request.method=='POST':
        #get info in login fields, verify it
        #if it works -> send to caligula ;)
        #if not -> back to login.html with error message
        username=request.form["username"]
        password=request.form["password"]
        #mongo stuff goes here
    if "user" not in session:
      session['user'] = username
    return redirect("/cladius")

@app.route("/cladius")
def test():
  if 'user' in session:#if logged in
    return render_template("cladius.html")
  else:
    return render_template('fail.html')


@app.route("/register")
def res():
    return render_template("register.html")

@app.route("/registering")
def regis():
    success = 0
    if request.method=='POST':
        #get the info from the fields
        #some verification (don't overlap with any name already in the databass
        #put into the database
        pass
    return redirect("/", success = success, logging = 0)


@app.route("/logout")
def logout():
    #remove session
    #return base (with message)
    session.pop('n',None)
    return redirect("/")

@app.route("/aboutLogIn")
def about():
    return render_template("Aenead.html")

@app.route("/DidYouSleep") #lolnever
def cheater():
    return render_template("Cladius.html")

@app.route("/Pokemon")
def hail():
    return render_template("Caesar.html")

if __name__=="__main__":
    app.secret_key="Don't put this on github"
    app.debug=True
    app.run()
