from todo_app.data import session_items, todo_items
from flask import Flask
from flask import render_template
from flask import request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', items=todo_items.get_todos())

@app.route('/', methods = ['POST'])
def post():
    todo_items.create_todo(request.form.get('title'))
    return render_template('index.html', items=todo_items.get_todos())

if __name__ == '__main__':
    app.run()
