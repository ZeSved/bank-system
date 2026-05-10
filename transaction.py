class Transaction: # The transaction class, simply for storing transacion data
  def __init__(self, amount, from_account=None, to_account=None):
    self.amount = amount
    self.from_account = from_account
    self.to_account = to_account