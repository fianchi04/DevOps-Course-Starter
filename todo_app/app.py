from todo_app.data import session_items
from flask import Flask
from flask import render_template
from flask import request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        session_items.add_item(request.form.get('title'))
        return render_template('index.html', items=session_items.get_items()) 
    if request.method == 'GET':
        return render_template('index.html', items=session_items.get_items())




if __name__ == '__main__':
    app.run()
