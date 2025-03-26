import api
import os
import pprint 
  
env_var = os.environ 
  
usuario = os.environ.get('USUARIO')
senha = os.environ.get('SENHA_API')

print(usuario, senha)

login = api.login(usuario, senha)
print(login)