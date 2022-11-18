#!/usr/bin/env python3
""" Mini Project 3 utilizing Flask and HTML Return """

# Project is a simulated app to submit name for a waitlist

from flask import Flask
from flask import session
from flask import url_for
from flask import escape
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)
app.secret_key = "AaBbCc"

data = [{
    "name": "default" }]

@app.route("/")
def start():
    # if the key "username" has a value
    if "username" in session:
        username = session["username"]
        name = username    
        return "You are on the waitlist!"

    return "You are not on the waitlist<br><a href = '/login'><b>Click to be added to Waitlist</b></a>"

## If the user hits /login with a GET or POST
@app.route("/login", methods = ["GET", "POST"])
def login():
   ## if you sent us a POST because you clicked the login button
   if request.method == "POST":
       ## request.form.get("xyzkey"): use get if the key might not exist
       session["username"] = request.form.get("username")
       data[0] = {"name":session["username"]}
       return redirect(url_for("start"))

   ## return this HTML data if you send us a GET
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/waitlist")
def waitlist():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

