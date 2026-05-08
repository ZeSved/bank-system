class Account:
  def __init__(self, name):
    self.name = name
    self.amount = 0
    self.transaction_history = []
  
  def deposit(self):
    while not (amount_to_deposit := input('Amount to deposit: ')).isdigit(): # Samma sak som while-loopen i förra
      amount_to_deposit = input('Amount to deposit: ')
    amount_to_deposit = int(amount_to_deposit)

    old_amount = self.amount

    if amount_to_deposit <= 0: # Ser till så att mängden att lägga in är mer än 0
      print('Invalid amount, must be above 0.')
    else:
      print(f'Successfully deposited {amount_to_deposit}, new amount {old_amount + amount_to_deposit}')
  
  def withdraw(self):
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
  
  def new_transaction(self, from_account, to_account, amount):
    transaction = {
      'from account': from_account,
      'to account': to_account,
      'amount': amount
    }

    self.transaction_history.append(transaction)