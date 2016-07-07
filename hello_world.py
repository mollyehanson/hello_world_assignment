from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

## python hello name
# @app.route("/hello/<name>")
# def hi_person(name):
#     return "Hello {}!".format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def hello_jedi(first_name, last_name):
    html = """
        <h1>
            Hello {}!
        </h1>
    """
    return html.format((last_name[:3]+first_name[:2]).title())

##python jedi name    
# @app.route("/jedi/<first_name>/<last_name>")
# def hi_jedi(first_name, last_name):
#     jedi_name = last_name[:3]+first_name[:2]
#     return "Hello {}!".format(jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            