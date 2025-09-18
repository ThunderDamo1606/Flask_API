from flask import Flask,request,redirect,url_for,session,Response

app1 = Flask(__name__)

#homepage Login page
@app1.route("/",methods =["GET","POST"])
def login():
    if request.method == "POSt":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username  #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid creditionals. Try again",mimetype="text/plain") #text/HTML
        

    return '''
           
'''