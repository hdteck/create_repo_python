#!/usr/bin/env python3
import yaml
import os
import sys
import requests
import json
from github import Github
from github import Auth
from pathlib import Path
# Nombre del archivo YAML proporcionado por el usuario
name_app = "${{ github.event.inputs.name_app }}"
file_path = f"./BBB-000/parameters.yml"
#sacamos el token del fichero .env
access_token = os.getenv('GITHUB_ACCESSTOKEN')

def create_project():
   token = os.environ['GITHUB_TOKEN']
   GITHUB_API_URL = "https://api.github.com/"
   headers = {"Authorization": "token {}".format(token)}
   data = {"name": "{}".format(reponame)}
   respuesta = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
   print(respuesta.status_code)
def create_branch():
    for ramas in {','.join(data['entornos_deploy'])}:
        rama = ramas.split(',')
        rama_number = 0
        print(rama[rama_number])
        token = os.environ['GITHUB_TOKEN']
        headers = {"Authorization": "token {}".format(token)}        
        url = "https://api.github.com/repos/"+"hdteck/reponame"+"/git/refs/heads"
        branches = requests.get(url, headers=headers).json()
#        sha = branches[-1]['object']['sha']
        res = requests.post("https://api.github.com/repos/"+"hdteck/"+reponame+"/git/refs", json={
              "ref": "refs/heads/"+rama[rama_number],
              "sha": "aa218f56b14c9653891f9e74264a383fa43fefbd"
                }, headers=headers)
        print(res.content)
        rama_number +=1
def create_codeowners_file():
    for users in {','.join(data['usuarios'])}:
        codeowners = users.split(',')
        usuario = 0
        fichero = Path("CODEOWNERS")
        if fichero.exists():
           f = open("CODEOWNERS","a")
           f.write("*"+"\t"+codeowners[usuario])
           f.close()
           usuario +=1        
        else:
           f = open("CODEOWNERS", "x")
           f.write("*"+"\t"+codeowners[usuario])
           f.close()
           usuario +=1
def create_ficheros_por_tecnologia():
    for tecnologias in {','.join(data['tecnologias'])}:
        tec = tecnologias.split(',')
        if tec == 'nodeJS':
            print("añadimos los ficheros necesarios para la tecnologia "+tec)
        elif tec == 'java':
            print("añadimos los ficheros necesarios para la tecnologia "+tec)
        elif tec == 'python':    
            print("añadimos los ficheros necesarios para la tecnologia "+tec)
# Leer el archivo YAML
with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
# es proyecto_producto
reponame = str({data['proyecto']}) +"_"+ str({data['producto']})
#print(f"aplicacion={data['aplicacion']}")
#print(f"producto={data['producto']}")
#print(f"proyecto={data['proyecto']}")
#print(f"tecnologias={','.join(data['tecnologias'])}")
#print(f"entornos_deploy={','.join(data['entornos_deploy'])}")
#print(f"usuarios={','.join(data['usuarios'])}")
#print(f"usuarios_aprobadores={','.join(data['usuarios_aprobadores'])}")


create_project()
create_branch()
create_codeowners_file()
create_ficheros_por_tecnologia()