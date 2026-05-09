class Transaction:
  def __init__(self, amount, from_account=None, to_account=None, from_user=None, to_user=None):
    self.amount = amount
    self.from_account = from_account
    self.to_account = to_account
    self.from_user = from_user
    self.to_user = to_user