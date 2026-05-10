def deposit(balance, amount):
	return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Error: Insufficient funds"
    return balance - amount
