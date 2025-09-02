#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
  
  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * self.discount / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if len(self.previous_transactions) > 0:
      last_trans = self.previous_transactions.pop()
      self.total -= last_trans["price"] * last_trans["quantity"]
      for _ in range(last_trans["quantity"]):
        self.items.pop()
    else:
      print("There are no previous transactions.")