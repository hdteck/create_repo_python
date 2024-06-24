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
#path es proyecto_producto
reponame = "data['proyecto']"+"_"+"data['producto']"
def create_project():
   token = os.environ['GITHUB_TOKEN']
   GITHUB_API_URL = "https://api.github.com/"
   headers = {"Authorization": "token {}".format(token)}
   data = {"name": "{}".format(reponame)}
   r = requests.post(GITHUB_API_URL +"hdteck/repos" + "", data=json.dumps(data), headers=headers)
   print(r)
def create_branch():
    for rama in {','.join(data['entornos_deploy'])}:
        user = Github(access_token).get_user()
        new_rama = user.get_branch(rama)
        user.create_git_ref(ref='refs/heads/' + rama, sha=new_rama.commit.sha)

# Leer el archivo YAML
with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
print(f"aplicacion={data['aplicacion']}")
print(f"producto={data['producto']}")
print(f"proyecto={data['proyecto']}")
print(f"tecnologias={','.join(data['tecnologias'])}")
print(f"entornos_deploy={','.join(data['entornos_deploy'])}")
print(f"usuarios={','.join(data['usuarios'])}")
print(f"usuarios_aprobadores={','.join(data['usuarios_aprobadores'])}")

#revisar el error 401 que aparece en la salida
create_project()
#create_branch()