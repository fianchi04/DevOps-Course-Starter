This app uses a Trello board to store and manage 'todo' and 'done' cards. To run the app and add/modify cards, two secrets are required.
To generate these secrets, you must have a [Trello account](https://trello.com/signup) and must generate an API key and token, [instructions on how to do that can be found here](https://trello.com/app-key). Add the following properties to the .env file in this project:
* TRELLO_KEY=**YOURAPIKEY**
* TRELLO_TOKEN=**YOURGENERATEDTOKEN**

The app is configured to use a pre-configured Trello Board, this can be changed by updating the List IDs in trello_client.py. Open the Trello board you wish to use, and find the List IDs by opening an existing card and appending .json to the end of the url. In the Json object, select the value for the "idList" property, and substitute that into trello_client.py for TODO_LIST_ID or DONE_LIST_ID.

For more information, see the [Trello FAQs](https://docs.n8n.io/nodes/n8n-nodes-base.trello/#example-usage).

