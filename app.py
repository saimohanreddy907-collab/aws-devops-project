from flask import Flask

app = Flask("aws-devops-app")

@app.route("/")
def home():
    return "<h1>AWS DevOps Project</h1><h2>Welcome to My Web Application!</h2><p>Successfully deployed using AWS, Jenkins and Docker.</p>"

app.run(host="0.0.0.0", port=5000)
