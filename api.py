from flask import Flask
from flask_restful import Api
from App.Config.database import *
from App.Routes import *
from App.Model.Pessoa import *
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    try:
        user = Pessoa.get(Pessoa.email == username)
        if user and safe_str_cmp(user.senha, password):
            return user
    except:
        return None

def identity(payload):
    try:
        user_id = payload['identity']
        return Pessoa.get(Pessoa.id == user_id)
    except:
        return None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWT(app, authenticate, identity)
routes(api)

if __name__ == '__main__':
    app.run(debug=True)