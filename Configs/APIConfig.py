import os
port = int(os.environ.get("PORT", 5000))
API = {
    'host': 'ai-tic-tac-toe-api.herokuapp.com',
    'version': '1.0.0',
    'port': port
};
APIPATH = '/api/v' + API['version']
