from bank_account import BankAccount

# Create account
account1 = BankAccount("Reema", 1000)

print("Account Holder:", account1.get_account_holder())
print("Initial Balance:", account1.get_balance())

# Deposit
try:
    new_balance = account1.deposit(500)
    print("Balance after deposit:", new_balance)
except ValueError as e:
    print("Error:", e)

# Withdraw
try:
    new_balance = account1.withdraw(200)
    print("Balance after withdrawal:", new_balance)
except Exception as e:
    print("Error:", e)

# Withdraw more than balance (to test exception)
try:
    account1.withdraw(5000)
except Exception as e:
    print("Error:", e)

print("Final Balance:", account1.get_balance())