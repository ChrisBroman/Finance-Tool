from itertools import count

month_list = {
  '1': 'January',
  '2': 'February',
  '3': 'March',
  '4': 'April',
  '5': 'May',
  '6': 'June',
  '7': 'July',
  '8': 'August',
  '9': 'September',
  '10': 'October',
  '11': 'November',
  '12': 'December'
}

class Transaction:
  id = count(0)
  def __init__(self, transaction):
    self.id = next(self.id)
    self.transaction = transaction
    self.date = transaction[0]
    self.name = transaction[1]
    self.amount = float(transaction[2])
    self.category = None

  def get_category(self):
    return self.category
  
  def get_id(self):
    return self.id

  def get_date(self):
    return self.date

  def get_name(self):
    return self.name

  def get_amount(self):
    return self.amount

  def set_category(self, category):
    self.category = category
