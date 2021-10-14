from todo_app.data import trello_client
from flask import Flask, redirect
from flask import render_template
from flask import request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html', todos=trello_client.get_todos(), dones=trello_client.get_dones())

@app.route('/card', methods = ['GET', 'POST'])
def post():
    trello_client.create_todo(request.form.get('title'))
    return redirect("/")

@app.route('/complete_card/<id>', methods = ['GET'])
def complete_card(id):
    print("here")
    trello_client.update_todo_change_list(id)
    return redirect("/")

if __name__ == '__main__':
    app.run()
