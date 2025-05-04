class BankAccount:
    DAILY_LIMIT = 25000
    TRANSACTION_LIMIT = 10000

    def __init__(self, balance):
        self.balance = balance
        self.daily_transferred = 0

    def transfer(self, amount):
        if amount > self.TRANSACTION_LIMIT:
            raise ValueError("Transfer exceeds per-transaction limit.")
        if self.daily_transferred + amount > self.DAILY_LIMIT:
            raise ValueError("Transfer exceeds daily transfer limit.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        self.daily_transferred += amount
        return True
