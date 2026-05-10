from transaction import Transaction

class Account: # Konto klassen
  def __init__(self, name, amount = 0, transaction_history = []):
    self.name = name
    self.amount = amount
    self.transaction_history = transaction_history
  
  def deposit(self, amount = None, external_transaction = None): # Lägger in pengar på kontot
    if amount is None:
      while not (amount_to_deposit := input('Amount to deposit: ')).isdigit(): # Ser till så att der är en siffra som läggs in och att den är stor nog
        try:
          if int(amount_to_deposit) < 0:
            print('Amount too low')
            return
        except:
          amount_to_deposit = input('Amount to deposit: ')
      amount_to_deposit = int(amount_to_deposit)
    else:
      amount_to_deposit = int(amount)

    old_amount = int(self.amount)

    self.amount = old_amount + amount_to_deposit
    
    if amount_to_deposit <= 0: # Ser till så att mängden att lägga in är mer än 0
      print('Invalid amount, must be above 0.')
    else:
      print(f'Successfully deposited {amount_to_deposit} into {self.name}, new amount {old_amount + amount_to_deposit}')
    
    if external_transaction is None: # Ifall det har skett en transaktion mellan konton
      self.new_transaction(Transaction(f'+{str(amount_to_deposit)}', None, self.name))
    else:
      self.new_transaction(external_transaction)
  
  def withdraw(self, amount = None, external_transaction = None): # Exakt samma som i förra men för att ta ut pengar
    if amount is None:
      while not (amount_to_withdraw := input('Amount to withdraw: ')).isdigit(): # Ser till så att det är en siffra användaren har skrivit in
        amount_to_withdraw = input('Amount to withdraw: ')
      amount_to_withdraw = int(amount_to_withdraw)
    else:
      amount_to_withdraw = int(amount)

    old_amount = self.amount
    old_amount = int(old_amount)

    if old_amount >= amount_to_withdraw: # Ser till så att man inte kan ta ut mer pengar än vad som finns
      new_amount = old_amount - amount_to_withdraw
      self.amount = new_amount
      print(f'{amount_to_withdraw} withdrawn from {self.name}, {new_amount} remaining')
    else:
      print('Invalid transaction, number too high.')
    
    if external_transaction is None: # Ifall det har skett en transaktion mellan konton
      self.new_transaction(Transaction(f'-{str(amount_to_withdraw)}', self.name))
    else:
      self.new_transaction(external_transaction)
  
  def new_transaction(self, transaction): # Lägger in ny transaktionshistorik i listan
    self.transaction_history.append(transaction)