import sys
clients = [
  { 
    'uid' : '0',
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer'
  },
  {
    'uid' : '1',
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data engineer'
  }
]

def create_client(client):
  global clients
  if client not in clients:
    clients.append(client)
  else:
    print('Client already is in the client\'s list')

def list_clients():
  for idx, client in enumerate(clients):
    print('{uid} | {name} | {company} | {email} | {position}'.format(
      uid = idx,
      name = client['name'],
      company = client['company'],
      email = client['email'],
      position = client['position']
    ))

def _get_id_client(client_name):
  for client in clients:
    if  client_name == client['name']:
      return client.get('uid')

def update_client(client_name, update_client_name):
  global clients
  if client_name in clients:
    index = clients.index(client_name)
    clients[index] = update_client_name
  else:
    print('Client is not in clients list')

def delete_client(id_client):
  global clients
  del clients[int(id_client)]


def search_client(client_name):
  for client in clients:
    if client != client_name:
      continue
    else:
      return True

def _print_welcome():
  print('Welcome to platzi ventas')
  print('*' * 50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')

def _get_client_field(field_name):
  field = None
  while not field:
    field = input('What is the client {}?'.format(field_name))
  return field

def _get_client_name():
  client_name = None
  while not client_name:
    client_name =  input('What is the client name?')
    if client_name == 'exit':
      client_name = None
      break

  if not client_name:
    sys.exit()
  return client_name

if __name__ == '__main__':
  _print_welcome()
  command = input('')
  command = command.upper()
  if command == 'C':
    client = {
      'uid' : len(clients) -1,
      'name': _get_client_field('name'),
      'company':_get_client_field('company'),
      'email': _get_client_field('email'),
      'position': _get_client_field('position')
    }
    create_client(client)
    list_clients()
  elif command == 'D':
    client_name = _get_client_field('name')
    id = _get_id_client(client_name)
    delete_client(id)
    list_clients()
  elif command == 'U':
    client_name = _get_client_name()
    update_client_name = input('What is the updated client name')
    update_client(client_name, update_client_name)
    list_clients()
  elif command == 'S':
    client_name = _get_client_name()
    found = search_client(client_name)
    if found:
      print('The client is in the client\'s list')
    else:
      print('The client : {} is not in our clients list'.format(client_name))
  else:
    print('Invalid command')