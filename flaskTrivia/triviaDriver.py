#!usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route("/") # user can land at "/"
def start():
    return render_template("trivia.html")

@app.route("/correct")
def correct():
    return "Correct Answer!\n"

@app.route("/trivia", methods = ["POST", "GET"])
def trivia():
    if request.method == "POST":
        if request.form.get("ans"): # if answer was given via the POST
            answer = request.form.get("ans") # grab the answer from the POST
            if (answer == "1"):
                return redirect("correct")
            else:
                return redirect("/")
        else: # if a user sent a post without answer, return to form
            return redirect("/")
            
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
