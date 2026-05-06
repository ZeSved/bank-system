import json
from user import User

USER_SAVE_FILE = './users.json'
DATA_SAVE_FILE = './data.json'

class Bank:
  def __init__(self):
    try:
      file = open('./users.json', 'r')
      file.close()
    except:
      with open('./users.json', 'w') as data: # Om den inte finns eller något fel har hänt, skapa en ny och hämta den
        data.write(json.dumps({}))

    try:
      file = open('./data.json', 'r')
      file.close()
    except:
      with open('./data.json', 'w') as data: # Om den inte finns eller något fel har hänt, skapa en ny och hämta den
        data.write(json.dumps({}))

    self.current_user = ''
    self.logged_in = False
  
  def new_user(self): # Skapar en ny användare
    name = input('Name: ')
    pin = input('PIN: ')

    current_user_data = {}

    self.current_user = name
    self.logged_in = True
    current_user_data['pin'] = pin
    current_user_data['saldo'] = 0

    self.buffer[name] = current_user_data

    self.operations()

  def log_in(self): # Loggar in användaren eller skapar nytt konto om inte namnet finns
    name = input('Name: ')

    names_file = open(USER_SAVE_FILE, 'r')
    names = json.load(names_file)
    
    if name in names['users']:
      names_file.close()
      pin = input('PIN: ')

      data_file = open(DATA_SAVE_FILE, 'r')
      data = json.load(data_file)
      
      if self.buffer[name]['pin'] == pin:
        self.logged_in = True
        self.current_user = name
      else:
        print('Incorrect PIN, please try again.')
    else:
      print("Couldn't find a user with that name.")
      self.new_user()
    
    self.operations()
    
  def log_out(self): # Loggar ut och sparar all data till databasen
    self.current_user = ''
    self.logged_in = False

    with open('./data.json', 'w') as data:
      data.write(json.dumps(self.buffer))
  
  def withdraw(self): # Tar ut pengar
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

    self.operations()
  
  def deposit(self): # Lägger in pengar
    while not (amount_to_deposit := input('Amount to deposit: ')).isdigit(): # Samma sak som while-loopen i förra
      amount_to_deposit = input('Amount to deposit: ')
    amount_to_deposit = int(amount_to_deposit)

    saldo = self.buffer[self.current_user]['saldo']
    self.buffer[self.current_user]['saldo'] = saldo + amount_to_deposit

    if amount_to_deposit <= 0: # Ser till så att mängden att lägga in är mer än 0
      print('Invalid amount, must be above 0.')
    else:
      print(f'Successfully deposited {amount_to_deposit}, new amount {saldo + amount_to_deposit}')
    self.operations()
  
  def check_amount(self): # Visar saldo
    print(f'Current amount in account: {self.buffer[self.current_user]['saldo']}')
    self.operations()

  def operations(self): # "Mitten" funktionen typ, kör efter majoriteten av andra funktioner
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