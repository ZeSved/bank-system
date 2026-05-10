from backend import backend
import random

class Bank:
  def __init__(self):
    self.logged_in = False
  
  def new_user(self): # Skapar en ny användare
    name = input('Name: ')
    pin = str(random.randint(1000, 9999))
    print(f'Your pin is {pin}')

    backend.new_user(name, pin)
    self.logged_in = True

    self.operations('main')

  def log_in(self): # Loggar in användaren eller skapar nytt konto om inte namnet finns
    name = input('Name: ')
    
    if backend.check_user_exists(name):
      pin = input('PIN: ')

      if backend.log_in(name, pin)['approved']:
        self.logged_in = True
      else:
        print('Incorrect PIN, please try again.')
        return
    else:
      print("Couldn't find a user with that name.")
      self.new_user()
    
    self.operations('main')
    
  def log_out(self): # Loggar ut och sparar all data till databasen
    self.logged_in = False

    backend.save_and_quit()

  def create_account(self):
    name = input('Account name: ')

    backend.create_account(name)

    self.operations('account')

  def delete_account(self):
    backend.delete_account()

    self.operations('main')

  def withdraw(self): # Tar ut pengar
    backend.opened_account.withdraw()
    self.operations('account')
  
  def deposit(self): # Lägger in pengar
    backend.opened_account.deposit()
    self.operations('account')
  
  def check_revenue(self): # Visar saldo
    print(f'Current amount in account: {backend.get_account_revenue()}')
    self.operations('account')

  def transaction(self):
    to_account = input('To bank account: ')
    amount = input('Amount to transfer: ')

    backend.transaction(backend.opened_account.name, to_account, amount)
    self.operations('main')
  
  def open_account(self):
    accounts = [account.name for account in backend.retrieve_accounts()]

    if len(accounts) == 0:
      print("You don't have any accounts")
      return self.operations('main')
    
    print('Your accounts:')
    for account in accounts:
      print(account)
    
    chosen_account = input('Which account would you like to open?: ')

    backend.open_account(chosen_account)

    self.operations('account')
  
  def transactions(self):
    for transaction in backend.opened_account.transaction_history:
      print(f"""
From account: {transaction.from_account}
To account: {transaction.to_account}
Amount: {transaction.amount}
""")
      
    self.operations('account')

  def operations(self, stage): # "Mitten" funktionen typ, kör efter majoriteten av andra funktioner
    main = """
1. Open account
2. Create account
3. Log out

> """

    account = """
1. Deposit
2. Withdraw
3. Check account revenue
4. Transfer to different account
5. Transaction history
6. Exit account
7. Delete account

> """

    if stage == 'main':
      operation = input(main)

      match operation:
        case '1':
          self.open_account()
        case '2':
          self.create_account()
        case '3':
          self.log_out()
    elif stage == 'account':
      operation = input(account)

      match operation:
        case '1':
          self.deposit()
        case '2':
          self.withdraw()
        case '3':
          self.check_revenue()
        case '4':
          self.transaction()
        case '5':
          self.transactions()
        case '6':
          backend.exit_account()
          self.operations('main')
        case '7':
          backend.delete_account()
          self.operations('main')

# Tekniskt sett hela systemet
bank = Bank()
command = ''
while command != '3':
  command = input(
"""
1. Sign up
2. Log in
3. Quit

> """)
  match command:
    case '1':
      bank.new_user()
    case '2':
      bank.log_in()