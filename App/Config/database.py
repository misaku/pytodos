from playhouse.dataset import DataSet
import os
import zipfile as zip

from App.Config.conection import db
from App.Model.Local import *
from App.Model.Pessoa import *
from App.Model.Tarefa import *

db.create_tables([Local,Pessoa,Tarefa])


def exportBkp():
    dbe = DataSet("postgresql://postgres:postgres@localhost:5432/my_app")
    tablePessoa = dbe['pessoa']
    tableLocal = dbe['local']
    tableTarefa = dbe['tarefa']                          
    dbe.freeze(tablePessoa.all(), format='json', filename='App/database/exported/pessoa.json')
    dbe.freeze(tableLocal.all(), format='json', filename='App/database/exported/local.json')
    dbe.freeze(tableTarefa.all(), format='json', filename='App/database/exported/tarefa.json')
    zf = zip.ZipFile('App/database/bkp.zip','w')
    for dirname, subdirs, files in os.walk('App/database/exported'):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname,filename))
    zf.close()

def importBkp():
    zf = zip.ZipFile('App/database/import/bkp.zip','r')
    zf.extractall('App/database/import')
    zf.close()
    dbe = DataSet("postgresql://postgres:postgres@localhost:5432/my_app")
    tablePessoa = dbe['pessoa']
    tableLocal = dbe['local']
    tableTarefa = dbe['tarefa'] 
    tablePessoa.thaw(format='json', filename='App/database/import/App/database/exported/pessoa.json')   
    tableLocal.thaw(format='json', filename='App/database/import/App/database/exported/local.json')   
    tableTarefa.thaw(format='json', filename='App/database/import/App/database/exported/tarefa.json')
