from App.Controller.PessoaController import *
from App.Controller.ExportController import *
from App.Controller.ImportController import *
from App.Controller.TarefaController import *
from App.Controller.LocalController import *
def routes(api):
    api.add_resource(ImportController, '/api/import')
    api.add_resource(ExportController, '/api/export')
    api.add_resource(PessoaControllerAll, '/api/pessoa')
    api.add_resource(PessoaController, '/api/pessoa/<int:user_id>')
    api.add_resource(LocalControllerAll, '/api/local')
    api.add_resource(LocalController, '/api/local/<int:local_id>')
    api.add_resource(TarefaControllerAll, '/api/tarefa')
    api.add_resource(TarefaController, '/api/tarefa/<int:tarefa_id>')