from App.Config.database import * 
from flask_restful import Resource, reqparse

class ImportController(Resource):
    def get(self):
        try:
            importBkp()
            res = True
        except:
            res = False
        return json.dumps({"data":res})
    