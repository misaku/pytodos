from App.Model.Pessoa import * 
from flask_restful import Resource, reqparse
from datetime import datetime
from flask import jsonify
from flask_jwt import jwt_required
import json

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('email')
parser.add_argument('senha')


class PessoaControllerAll(Resource):
    def get(self):
        try:
            user = Pessoa.select().dicts()
            res = [u for u in user]
        except:
            res = []
        return json.dumps({"data":res})
    
    def post(self):
        args = parser.parse_args()
        try:
            user = Pessoa()
            if(args['nome'] != None):
                user.nome = args['nome']
            if(args['email'] != None):
                user.email = args['email']
            if(args['senha'] != None):
                user.senha = args['senha']
            user.save()
            res = Pessoa.select().where(Pessoa.id==user.id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})

class PessoaController(Resource):
    decorators = [jwt_required()]
    def get(self, user_id):
        try:
            res = Pessoa.select().where(Pessoa.id==user_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    def put(self, user_id):
        args = parser.parse_args()
        try:
            user = Pessoa.get(Pessoa.id==user_id)
            if(args['nome'] != None):
                user.nome = args['nome']
            if(args['email'] != None):
                user.email = args['email']
            if(args['senha'] != None):
                user.senha = args['senha']
            user.save()
            res = Pessoa.select().where(Pessoa.id==user_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    
    def delete(self, user_id):
        try:
            user = Pessoa.get(Pessoa.id==user_id)
            user.delete_instance()
            res = True
        except:
            res = False
        return json.dumps({"data":res})
