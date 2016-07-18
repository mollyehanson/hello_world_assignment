from flask import Flask
from os import environ
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def template_test():
    t = Template("Hello {{ something }}!")
    return t.render(something="World")

@app.route("/jedi/<first_name>/<last_name>")
def hello_jedi(first_name, last_name):
    t = Template("My jedi name is {{last_name}}{{first_name}}")
    return t.render(first_name=first_name[:2], last_name=last_name[:3])

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            