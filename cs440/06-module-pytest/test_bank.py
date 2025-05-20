from bank import BankAccount
import pytest

def test_valid_transfer():
    account = BankAccount(30000)
    assert account.transfer(5000) == True
    assert account.balance == 25000

def test_exceeds_transaction_limit():
    account = BankAccount(50000)
    with pytest.raises(ValueError, match="per-transaction limit"):
        account.transfer(15000)

def test_exceeds_daily_limit():
    account = BankAccount(50000)
    account.transfer(15000)
    with pytest.raises(ValueError, match="daily transfer limit"):
        account.transfer(11000)

def test_insufficient_funds():
    account = BankAccount(5000)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.transfer(6000)

# corrected test_exceeds_daily_limit
def test_exceeds_daily_limit():
    account = BankAccount(50000)
    account.transfer(9000)  # total = 9000
    account.transfer(9000)  # total = 18000
    with pytest.raises(ValueError, match="daily transfer limit"):
        account.transfer(8000)  # total would become 26000 > 25000 daily cap
