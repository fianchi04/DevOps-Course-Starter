import requests, os
from dotenv import load_dotenv

from todo_app.model.Card import Card

TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_KEY = os.getenv("TRELLO_KEY")
TODO_LIST_ID = "6165ed85c7acb11e1c5f4f59"
DONE_LIST_ID = "6165ed85c7acb11e1c5f4f5b"

# API Client for Trello Board, see UsingTrello.md 
# and Trello API Docs: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-get

def create_todo_url(name):
    return "https://api.trello.com/1/cards?idList=6165ed85c7acb11e1c5f4f59&key="+TRELLO_KEY+"&token="+TRELLO_TOKEN+"&name="+name

def create_todo(name):
    url = create_todo_url(name)
    create_todo_response = requests.post(url)
    print(create_todo_response)

def get_cards_url(list_id):
    return "https://api.trello.com/1/lists/"+list_id+"/cards"

def get_todos():
    todos_json = requests.get(get_cards_url(TODO_LIST_ID)).json()
    todos = []
    for todo in todos_json:
        todos.append ( Card( id = todo['id'], title = todo['name'], status= 'Done'))
    return todos

def get_dones():
    dones_json = requests.get(get_cards_url(DONE_LIST_ID)).json()
    dones = []
    for done in dones_json:
        dones.append ( Card( id = done['id'], title = done['name'], status= 'Done'))
    return dones


def update_todo_change_list_url(id, new_board_id):
    return "https://api.trello.com/1/cards/"+id+"?idList="+new_board_id+"&key="+TRELLO_KEY+"&token="+TRELLO_TOKEN

def update_todo_change_list(id):
    requests.put(update_todo_change_list_url(id, DONE_LIST_ID))


