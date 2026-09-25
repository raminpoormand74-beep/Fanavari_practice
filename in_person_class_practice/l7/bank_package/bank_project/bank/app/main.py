from .calculator import deposit
from ..account import show_balance
from ..fees import apply_fee


balance = 1000

print(show_balance(balance))

balance = deposit(balance, 500)
print(show_balance(balance))

balance = apply_fee(balance, 50)
print(show_balance(balance))