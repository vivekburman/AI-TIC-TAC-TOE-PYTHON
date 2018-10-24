from Controllers.Info import Info
from Controllers.FetchMoveController import FetchMoveController
from app import *
from flask_cors import CORS, cross_origin

api.add_resource(Info, apiPath + "/info")
api.add_resource(FetchMoveController,
    apiPath + "/get-next-move",
    endpoint = "get_next_move"
)
api.add_resource(FetchMoveController,
    apiPath + "/get-winner",
    endpoint = "get_winner"
)
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=APIConfig.API['port'], threaded=True)
