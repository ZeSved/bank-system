import json
import os
from user import User

USER_SAVE_FILE = './users.json'
DATA_SAVE_PATH = './user_data/'

class _Backend:
  def __init__(self):
    self.current_user = ''
    self.save_file_path = ''
    self.opened_account = None

    if not os.path.exists(USER_SAVE_FILE):
      with open(USER_SAVE_FILE, 'w') as data: # Om den inte finns eller något fel har hänt, skapa en ny och hämta den
        data.write(json.dumps({'users': []}))

    if not os.path.exists(DATA_SAVE_PATH):
      os.mkdir(DATA_SAVE_PATH)
  
  def check_user_exists(self, user):
    with open(USER_SAVE_FILE, 'r') as file:
      return user in file['users']
  
  def check_pin(self, name, pin):
    save_file_path = f'{DATA_SAVE_PATH}{name}{pin}.json'

    if os.path.exists(save_file_path):
      self.save_file_path = save_file_path
      with open(self.save_file_path, 'r') as file:
        data = json.load(file)

        user = User(name, pin, data['accounts'], data['transactions'])

        self.current_user = user

        return {'approved': True}
    else:
      return {'approved': False}
  
  def save_and_quit(self):
    with open(self.save_file_path, 'w') as file:
      data = {
        'accounts': self.current_user.accounts,
        'transactions': self.current_user.transactions
      }

      file.write(json.dumps(data))

      self.current_user = ''
      self.save_file_path = ''
  
  def new_user(self, name, pin):
    with open(USER_SAVE_FILE, 'r+') as file:
      data = json.load(file)

      data['users'].append(name)

      file.write(json.dumps(data))
    
    user = User(name, pin, [], [])
    self.current_user = user
  
  def retrieve_accounts(self):
    return self.current_user.accounts
  
  def open_account(self, name):
    for account in self.current_user.accounts:
      if account.name == name: self.opened_account = account
  
  def exit_account(self):
    index = -1

    for account in self.current_user.accounts:
      index += 1

      if account.name == self.opened_account.name:
        break
    
    self.current_user.accounts[index] = self.opened_account

    self.opened_account = None
  
  def get_account_revenue(self):
    return self.opened_account.amount


backend = _Backend()