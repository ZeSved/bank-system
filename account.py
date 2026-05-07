class Account:
  def __init__(self, name):
    self.name = name
    self.amount = 0
    self.transaction_history = []
  
  def deposit(self):
    while not (amount_to_deposit := input('Amount to deposit: ')).isdigit(): # Samma sak som while-loopen i förra
      amount_to_deposit = input('Amount to deposit: ')
    amount_to_deposit = int(amount_to_deposit)

    saldo = self.buffer[self.current_user]['saldo']
    self.buffer[self.current_user]['saldo'] = saldo + amount_to_deposit

    if amount_to_deposit <= 0: # Ser till så att mängden att lägga in är mer än 0
      print('Invalid amount, must be above 0.')
    else:
      print(f'Successfully deposited {amount_to_deposit}, new amount {saldo + amount_to_deposit}')
  
  def withdraw(self):
    while not (amount := input('Amount to withdraw: ')).isdigit(): # Ser till så att mängden är en siffra
      amount = input('Amount to withdraw: ')
    amount = int(amount)

    saldo = self.buffer[self.current_user]['saldo']

    if saldo >= amount: # Ser till så att man inte kan ta ut mer pengar än vad som finns
      new_amount = saldo - amount
      self.buffer[self.current_user]['saldo'] = new_amount
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