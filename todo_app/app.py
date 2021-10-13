from todo_app.data import session_items, todo_items
from flask import Flask
from flask import render_template
from flask import request


from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo_items.create_todo()
        session_items.add_item(request.form.get('title'))
        return render_template('index.html', items=session_items.get_items()) 
        ##todo: separate routes for adding todo https://github.com/fianchi04/DevOps-Course-Starter/pull/1#discussion_r628209452

    if request.method == 'GET':
        return render_template('index.html', items=session_items.get_items())


if __name__ == '__main__':
    app.run()
