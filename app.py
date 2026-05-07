import json
from user import User
from memory import database
import random

class Bank:
  def __init__(self):
    self.logged_in = False
  
  def new_user(self): # Skapar en ny användare
    name = input('Name: ')
    pin = random.randint(1000, 9999)
    print(f'Your pin is {pin}')

    database.new_user(name, pin)
    self.logged_in = True

  def log_in(self): # Loggar in användaren eller skapar nytt konto om inte namnet finns
    name = input('Name: ')
    
    if database.check_user_exists(name):
      pin = input('PIN: ')

      if database.check_pin(name, pin):
        self.logged_in = True
      else:
        print('Incorrect PIN, please try again.')
    else:
      print("Couldn't find a user with that name.")
      self.new_user()
    
    self.operations()
    
  def log_out(self): # Loggar ut och sparar all data till databasen
    self.logged_in = False

    database.save_and_quit()
  
  def withdraw(self): # Tar ut pengar
    pass
  
  def deposit(self): # Lägger in pengar
    pass
  
  def check_amount(self): # Visar saldo
    print(f'Current amount in account: {self.buffer[self.current_user]['saldo']}')
    self.operations()

  def operations(self, stage): # "Mitten" funktionen typ, kör efter majoriteten av andra funktioner
    main = """
1. Open account
2. Create account
3. Log out
"""

    account = """
1. Deposit
2. Withdraw
3. Check account revenue
4. Transfer to different account
5. Transaction history
6. Exit account
"""
    operaiton = input("""
1. Open account
2. Deposit
3. Withdraw
4. Check account
5. Log out
""")
    match operaiton:
      case '1':
        self.open_account()
      case '2':
        self.deposit()
      case '3':
        self.withdraw()
      case '4':
        self.check_amount()
      case '5':
        self.log_out()

# Tekniskt sett hela systemet
bank = Bank()
command = ''
while command != '3':
  command = input(
"""
1. Sign up
2. Log in
3. Quit
""")
  match command:
    case '1':
      bank.new_user()
    case '2':
      bank.log_in()