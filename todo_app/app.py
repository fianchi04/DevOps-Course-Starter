from todo_app.data import session_items, todo_items
from flask import Flask
from flask import render_template
from flask import request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html', todos=todo_items.get_todos(), dones=todo_items.get_dones())

@app.route('/card', methods = ['GET', 'POST'])
def post():
    todo_items.create_todo(request.form.get('title'))
    return render_template('index.html', todos=todo_items.get_todos(), dones=todo_items.get_dones())

#def update_card_list():


if __name__ == '__main__':
    app.run()
