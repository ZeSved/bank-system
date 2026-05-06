class Account:
  def __init__(self, name):
    self.name = name
    self.amount = 0
    self.transaction_history = []
  
  def deposit(self, amount):
    self.amount += amount
  
  def withdraw(self, amount):
    self.amount -= amount
  
  def new_transaction(self, from_account, to_account, amount):
    transaction = {
      'from account': from_account,
      'to account': to_account,
      'amount': amount
    }

    self.transaction_history.append(transaction)