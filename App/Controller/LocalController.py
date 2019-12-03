from App.Model.Local import * 
from flask_restful import Resource, reqparse
from datetime import datetime
from flask import jsonify
from flask_jwt import jwt_required
import json

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('endereco')


class LocalControllerAll(Resource):
    decorators = [jwt_required()]
    def get(self):
        try:
            local = Local.select().dicts()
            res = [u for u in local]
        except:
            res = []
        return json.dumps({"data":res})
    
    def post(self):
        args = parser.parse_args()
        try:
            local = Local()
            if(args['nome'] != None):
                local.nome = args['nome']
            if(args['endereco'] != None):
                local.endereco = args['endereco']
            local.save()
            res = Local.select().where(Local.id==local.id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})

class LocalController(Resource):
    decorators = [jwt_required()]
    def get(self, local_id):
        try:
            res = Local.select().where(Local.id==local_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    def put(self, local_id):
        args = parser.parse_args()
        try:
            local = Local.get(Local.id==local_id)
            if(args['nome'] != None):
                local.nome = args['nome']
            if(args['endereco'] != None):
                local.endereco = args['endereco']
            local.save()
            res = Local.select().where(Local.id==local_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    
    def delete(self, local_id):
        try:
            local = Local.get(Local.id==local_id)
            local.delete_instance()
            res = True
        except:
            res = False
        return json.dumps({"data":res})
