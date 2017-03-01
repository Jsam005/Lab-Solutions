<<<<<<< HEAD

class CheckingAccount:

    def __init__(self,first_name,last_name,*args,**kwargs):

        self.first_name = first_name

        self.last_name = last_name

        self.balance = 0.00

        self.transaction_history = []

        self.withdrawal_total = 0

        self.deposit_total = 0

    def to_deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.deposit_total += deposit_amount
        print("You deposited {} into you account".format(float(int(deposit_amount))))

        deposit_history = ("Deposit: ${}".format(float(int(deposit_amount))))
        self.transaction_history.append(deposit_history)

    def to_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Insufficient funds, your remaining balance is ${}.".format(float(int(self.balance))))
        else:
            self.balance -= withdrawal_amount
            self.withdrawal_total += withdrawal_amount
            print("You withdrew {} from your account".format(float(int(withdrawal_amount))))

            withdraw_history = ("Withdrawal: ${}".format(float(int(withdrawal_amount))))
            self.transaction_history.append(withdraw_history)

    def get_transaction_history(self):
        return self.transaction_history

    def get_withdrawal_total(self):

        total = 0

        for amount in self.withdrawal_total:
            total += amount
            return total

    def get_deposit_total(self):

        total = 0

        for money in self.deposit_total:
            total += money
            return total

    def get_balance(self):
        balance_history = ("Checked balance: ${}".format(self.balance))
        self.transaction_history.append(balance_history)
        return self.balance

=======

class CheckingAccount:

    def __init__(self,first_name,last_name,*args,**kwargs):

        self.first_name = first_name

        self.last_name = last_name

        self.balance = 0.00

        self.transaction_history = []

        self.withdrawal_total = 0

        self.deposit_total = 0

    def to_deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.deposit_total += deposit_amount
        print("You deposited {} into you account".format(float(int(deposit_amount))))

        deposit_history = ("Deposit: ${}".format(float(int(deposit_amount))))
        self.transaction_history.append(deposit_history)

    def to_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Insufficient funds, your remaining balance is ${}.".format(float(int(self.balance))))
        else:
            self.balance -= withdrawal_amount
            self.withdrawal_total += withdrawal_amount
            print("You withdrew {} from your account".format(float(int(withdrawal_amount))))

            withdraw_history = ("Withdrawal: ${}".format(float(int(withdrawal_amount))))
            self.transaction_history.append(withdraw_history)

    def get_transaction_history(self):
        return self.transaction_history

    def get_withdrawal_total(self):

        total = 0

        for amount in self.withdrawal_total:
            total += amount
            return total

    def get_deposit_total(self):

        total = 0

        for money in self.deposit_total:
            total += money
            return total

    def get_balance(self):
        balance_history = ("Checked balance: ${}".format(self.balance))
        self.transaction_history.append(balance_history)
        return self.balance

>>>>>>> 574234176bcf2e44479089cb8f356b25c48b5c71
