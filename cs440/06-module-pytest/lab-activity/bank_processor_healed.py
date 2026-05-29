# Bank Processing & Verification Layer - Project Horizon Baseline
import sys

class BankAccount:
    DAILY_LIMIT = 25000
    TRANSACTION_LIMIT = 10000

    def __init__(self, balance):
        self.balance = balance
        self.daily_transferred = 0

    def transfer(self, amount):
        # Limit Requirement 1: Per-transaction ceiling verification
        if amount > self.TRANSACTION_LIMIT:
            raise ValueError("Transfer exceeds per-transaction limit.")
        # Limit Requirement 2: Cumulative daily volume calculation
        if self.daily_transferred + amount > self.DAILY_LIMIT:
            raise ValueError("Transfer exceeds daily transfer limit.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
            
        self.balance -= amount
        self.daily_transferred += amount
        return True

def verify_limits():
    print("[*] Running system limit boundary test suite...")
    account = BankAccount(50000)
    
    # FAULT: The verification logic intends to audit the cumulative daily threshold ($25,000).
    # However, it attempts a single transfer of $15,000 first.
    # This prematurely trips the per-transaction limit logic ($10,000), masking the downstream validation.
    account.transfer(9000)  # Safe Transaction 1
    account.transfer(9000)  # Safe Transaction 2 (Total: 18000)
    try:
        account.transfer(8000)  # Pushes aggregate to 26000 (Triggers Daily Limit)
        raise AssertionError('TestFailed: Daily limit check bypassed.')
    except ValueError as e:
        if 'daily transfer limit' in str(e):
            print('[+] Success: Daily transfer limit guard verified successfully.')
        else:
            raise e 
    
    print("[+] Boundary check suite processed successfully.")

if __name__ == "__main__":
    verify_limits()