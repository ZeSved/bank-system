from transaction import Transaction

class Account:
  def __init__(self, name, amount = 0, transaction_history = []):
    self.name = name
    self.amount = amount
    self.transaction_history = transaction_history
  
  def deposit(self, external_transaction = None):
    while not (amount_to_deposit := input('Amount to deposit: ')).isdigit(): # Samma sak som while-loopen i förra
      amount_to_deposit = input('Amount to deposit: ')
    amount_to_deposit = int(amount_to_deposit)

    old_amount = self.amount

    self.amount = old_amount + amount_to_deposit
    
    if amount_to_deposit <= 0: # Ser till så att mängden att lägga in är mer än 0
      print('Invalid amount, must be above 0.')
    else:
      print(f'Successfully deposited {amount_to_deposit}, new amount {old_amount + amount_to_deposit}')
    
    if external_transaction is None:
      self.new_transaction(Transaction(f'+{str(amount_to_deposit)}', None, self.name))
    else:
      self.new_transaction(external_transaction)
  
  def withdraw(self, external_transaction = None):
    while not (amount := input('Amount to withdraw: ')).isdigit(): # Ser till så att mängden är en siffra
      amount = input('Amount to withdraw: ')
    amount = int(amount)

    old_amount = self.amount

    if old_amount >= amount: # Ser till så att man inte kan ta ut mer pengar än vad som finns
      new_amount = old_amount - amount
      self.amount = new_amount
      print(f'{amount} withdrawn, {new_amount} remaining')
    else:
      print('Invalid transaction, number too high.')
    
    if external_transaction is None:
      self.new_transaction(Transaction(f'-{str(amount)}', self.name))
    else:
      self.new_transaction(external_transaction)
  
  def new_transaction(self, transaction):
    self.transaction_history.append(transaction)