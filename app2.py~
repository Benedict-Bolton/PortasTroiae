# Everything was a little messy in the other file, just trying to keep it okay

def check(function):
    def inner(*args):
        if "logged" not in session:
            session['logged'] = False
        if 'user' not in session:
            session['user'] = ""

        if "logging" in session:
            logging = session["logging"]
            print logging
            session.pop("logging", None)
            if logging:
                return render_template("home.html", logging = logging, logged = session['logged'], user = session['user'])
            else:
                return render_template("login.html", logging = logging, logged = session['logged'], user = session['user'])

        if "success" in session:
        success = session["success"]
        session.pop("success", None)
        if success:
            return render_template("login.html", success = success, logged = session['logged'], user = session['user'])
        else:
            return render_template("register.html", success = success, logged = session['logged'], user = session['user'])
    
    return inner

