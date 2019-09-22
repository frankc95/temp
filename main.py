from flask import Flask, render_template      
app = Flask('app')

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

app.run(host ='0.0.0.0', debug=True)

