import json
import os
from user import User
from account import Account
from transaction import Transaction
from pathlib import Path

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
    elif os.path.exists(USER_SAVE_FILE):
      file = open(USER_SAVE_FILE, 'r')
      if file.readline() == '':
        file.close()
        with open(USER_SAVE_FILE, 'w') as data:
          data.write(json.dumps({'users': []}))

    if not os.path.exists(DATA_SAVE_PATH):
      os.mkdir(DATA_SAVE_PATH)
    
  def check_user_exists(self, name):
    with open(USER_SAVE_FILE, 'r') as file:
      data = json.load(file)
      
      return name in data['users']
  
  def check_pin(self, name, pin):
    save_file_path = f'{DATA_SAVE_PATH}{name}{pin}.json'
    path = Path(save_file_path)

    if path.exists():
      self.save_file_path = save_file_path
      return True
    else: return False
    
  def log_in(self, name, pin):
    print(name, pin, 'login')
    if self.check_pin(name, pin):
      with open(self.save_file_path, 'r') as file:
        data = json.load(file)

        account_arr = []
        for account in data['accounts']:
          acc_class = Account(name=account['name'], amount=account['amount'], transaction_history=account['transaction history'])

          transaction_arr = []
          for transaction in account['transaction history']:
            trans_class = Transaction(
              amount=transaction['amount'],
              from_account=transaction['from_account'],
              to_account=transaction['to_account'],
              from_user=transaction['from_user'],
              to_user=transaction['to_user']
            )

            transaction_arr.append(trans_class)
          
          acc_class.transaction_history = transaction_arr
          
          account_arr.append(acc_class)

        self.current_user = User(name, pin, account_arr)

        print(self.current_user, 'user')
        print(self.save_file_path, 'save file path')
        return {'approved': True}
    else:
      return {'approved': False}
  
  def new_user(self, name, pin):
    self.save_file_path = f'{DATA_SAVE_PATH}{name}{pin}.json'

    with open(USER_SAVE_FILE, 'r') as file:
      data = json.load(file)

    data['users'].append(name)

    with open(USER_SAVE_FILE, 'w') as file:
      file.write(json.dumps(data))
    
    user = User(name, pin, [])
    self.current_user = user
  
  def create_account(self, name):
    account = Account(name)

    self.current_user.accounts.append(account)
    self.opened_account = account
  
  def retrieve_accounts(self):
    return self.current_user.accounts
  
  def open_account(self, name):
    for account in self.retrieve_accounts():
      if account.name == name: self.opened_account = account
  
  def get_account_revenue(self):
    return self.opened_account.amount
  
  def get_account_index(self, name):
    index = -1

    for account in self.retrieve_accounts():
      index += 1

      if account.name == name: return index
  
  def exit_account(self):
    index = self.get_account_index(self.opened_account.name)
    
    self.current_user.accounts[index] = self.opened_account

    self.opened_account = ''
  
  def delete_account(self):
    pin = input('PIN code: ')
    if not self.current_user.code == pin:
      return print('Incorrect PIN.')

    for account in self.retrieve_accounts():
      if account.name == self.opened_account.name:
        del self.current_user.accounts[self.get_account_index(self.opened_account.name)]

        return print("Account deleted successfully.")
      
    return print('Account not found.')
  
  def transaction(self, from_account, to_account, amount, to_user = None, current_user_pin = None, receiving_user_pin = None):

    def withdraw(account, amount):
      self.open_account(account)
      self.opened_account.withdraw(amount)
      self.exit_account()
    
    def deposit(account, amount):
      self.open_account(account)
      self.opened_account.deposit(amount)
      self.exit_account()
      
    withdraw(from_account, amount)

    deposit(to_account, amount)
   
  def save_and_quit(self):
    with open(self.save_file_path, 'w') as file:
      account_arr = []

      for account in self.retrieve_accounts():
        transaction_arr = []

        for trans in account.transaction_history:
          trans_data = {
            'amount': trans.amount,
            'from_account': trans.from_account,
            'to_account': trans.to_account,
            'from_user': trans.from_user,
            'to_user': trans.to_user
          }

          transaction_arr.append(trans_data)
        
        account_data = {
          'name': account.name,
          'amount': account.amount,
          'transaction history': transaction_arr
        }

        account_arr.append(account_data)

      data = {
        'accounts': account_arr
      }

      file.write(json.dumps(data))

      self.current_user = ''
      self.save_file_path = ''

backend = _Backend()