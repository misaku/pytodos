from App.Model.Tarefa import * 
from flask_restful import Resource, reqparse
from datetime import datetime
from flask import jsonify
from flask_jwt import jwt_required
import json

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('descricao')
parser.add_argument('pessoa')
parser.add_argument('contato')
parser.add_argument('local')
parser.add_argument('feita')

class TarefaControllerAll(Resource):
    decorators = [jwt_required()]
    def get(self):
        try:
            tarefa = Tarefa.select().dicts()
            res = [u for u in tarefa]
        except:
            res = []
        return json.dumps({"data":res})
    
    def post(self):
        args = parser.parse_args()
        try:
            tarefa = Tarefa()
            if(args['nome'] != None):
                tarefa.nome = args['nome']
            if(args['descricao'] != None):
                tarefa.descricao = args['descricao']
            if(args['pessoa'] != None):
                tarefa.pessoa = args['pessoa']
            if(args['contato'] != None):
                tarefa.contato = args['contato']
            if(args['local'] != None):
                tarefa.local = args['local']
            if(args['feita'] != None):
                tarefa.feita = args['feita']
            tarefa.save()
            res = Tarefa.select().where(Tarefa.id==tarefa.id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})

class TarefaController(Resource):
    decorators = [jwt_required()]
    def get(self, tarefa_id):
        try:
            res = Tarefa.select().where(Tarefa.id==tarefa_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    def put(self, tarefa_id):
        args = parser.parse_args()
        try:
            tarefa = Tarefa.get(Tarefa.id==tarefa_id)
            if(args['nome'] != None):
                tarefa.nome = args['nome']
            if(args['descricao'] != None):
                tarefa.descricao = args['descricao']
            if(args['pessoa'] != None):
                tarefa.pessoa = args['pessoa']
            if(args['contato'] != None):
                tarefa.contato = args['contato']
            if(args['local'] != None):
                tarefa.local = args['local']
            if(args['feita'] != None):
                tarefa.feita = args['feita']
            tarefa.save()
            res = tarefa.select().where(Tarefa.id==tarefa_id).dicts().get()
        except:
            res = None
        return json.dumps({"data":res})
    
    
    def delete(self, tarefa_id):
        try:
            tarefa = Tarefa.get(Tarefa.id==tarefa_id)
            tarefa.delete_instance()
            res = True
        except:
            res = False
        return json.dumps({"data":res})
