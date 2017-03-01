from bank_account import CheckingAccount

person = CheckingAccount('Jamie', 'Sam')


def main():

    using = True

    while using:

        bank_option = (input("Hello {} {}. Pick from the following options: 1. Deposit Money 2. Withdraw Money 3. Check Balance 4. View Transactions 5. Quit".format(person.first_name,person.last_name)))

        print(bank_option)

        if bank_option == "1":
            deposit_amount = float(int(input("Enter the amount you would like to deposit: $")))
            print(deposit_amount)
            person.to_deposit(deposit_amount)


        elif bank_option == "2":
            withdrawal_amount = float(int(input("Enter the amount you would like to withdraw: $")))
            print(withdrawal_amount)
            person.to_withdrawal(withdrawal_amount)

        elif bank_option == "3":
            print(person.get_balance())

        elif bank_option == "4":
            print(person.get_transaction_history())

        elif bank_option == "5":
            using = False
            print("Goodbye {} {}. Your total deposits for this session was ${} and your total withdrawals for this session was ${}. The final balance in your account is ${}.".format(
                    person.first_name, person.last_name, person.deposit_total, person.withdrawal_total, person.balance))
            break

main()
