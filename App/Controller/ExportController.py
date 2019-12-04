from App.Config.database import * 
from flask_restful import Resource, reqparse

class ExportController(Resource):
    def get(self):
        try:
            exportBkp()
            res = True
        except:
            res = False
        return json.dumps({"data":res})
    