class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    # Getter methods
    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    # setter methods
    def set_account_number(self, account_number):
        if isinstance(account_number, str):
            self._account_number = account_number
        else:
            print("Error: Account number must be a string.")

# Example usage
if __name__ == "__main__":
    # Create an account
    my_account = BankAccount(account_number="123456789",
                             account_holder="Fred Bloggs", balance=1000.0)

    print("Account Number:", my_account.get_account_number())
    print("Account Holder:", my_account.get_account_holder())
    print("Balance:", my_account.get_balance())

    my_account.set_account_number("123")
    print("Account number:", my_account._account_number)