from flask import Flask,request,redirect,render_template,session
from pymongo import Connection,MongoClient

################################ mongo stuff ############################ 
client = MongoClient()
db = client['portas-troiae']
#collection = db['user-info']

def add(username,password):
    #adds to the database
    db.users.insert({'name': username, 'password': password})

def check(username, password):
    #makes sure the usrname and password are valid





################################ webapp stuff ###########################
app=Flask(__name__)

@app.route("/")
def base():
    success = 0
    logging = 0
    if 'n' not in session:
        session['n']= "save in session"
        return "session set"
    else:
        return sessions['n']
    return render_template("login.html", success = success, logging = logging)

@app.route("/logging", methods=['POST'])
def index():
    if request.method=='POST':
        #get info in login fields, verify it                                 
        #if it works -> send to caligula ;)                                  
        #if not -> back to login.html with error message                     
    return render_template("index.html",logging = logging, success = 0)

@app.route("/register")
def res():
    return render_template("register.html")

@app.route("/registering")
def regis:
    success = 0
    if request.method=='POST':
        #get the info from the fields                                        
        #some verification (don't overlap with any name already in the datab\
ase)                                                                         
        #put into the database                                               
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

@app.route("/DidYouSleep")
def cheater():
    return render_template("Cladius.html")

@app.route("/Pokemon")
def hail():
    return render_template("Caesar.html")

if __name__=="__main__":
    app.secret_key="Don't put this on github"
    app.debug=True
    app.run()