#!/usr/bin/env python3
import yaml
import os
import sys
import requests
import json
from github import Github
from github import Auth
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
        print(rama[0])
        token = os.environ['GITHUB_TOKEN']
        headers = {"Authorization": "token {}".format(token)}
        url = "https://api.github.com/repos/"+"hdteck/reponame"+"/git/refs/heads"
        branches = requests.get(url, headers=headers).json()
        branch, sha = branches[-1]['ref'], branches[-1]['object']['sha']
        url_new_branch = "https://api.github.com/repos/"+"hdteck/reponame"+"/git/refs"
        res = requests.post(url_new_branch, json={
             "ref": "refs/heads/rama[0]",
             "sha": sha
             }, headers=headers)
        print(res.content)

# Leer el archivo YAML
with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
# es proyecto_producto
reponame = str({data['proyecto']}) +"_"+ str({data['producto']})
print(f"aplicacion={data['aplicacion']}")
print(f"producto={data['producto']}")
print(f"proyecto={data['proyecto']}")
print(f"tecnologias={','.join(data['tecnologias'])}")
print(f"entornos_deploy={','.join(data['entornos_deploy'])}")
print(f"usuarios={','.join(data['usuarios'])}")
print(f"usuarios_aprobadores={','.join(data['usuarios_aprobadores'])}")

#revisar el error 401 que aparece en la salida
create_project()
create_branch()