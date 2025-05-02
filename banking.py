balance = 5000


def deposit(amount):
    global balance
    if amount > 0:
        balance = amount + balance
        print(f"Deposit successful! New balance: {balance}")
    else:
        print("Deposit amount must be positive.")


def withdraw(amount):
    global balance
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! New balance: {balance}")
    else:
        print("Withdrawal amount must be positive and less than or equal to the balance.")


def check_balance():
    print(f"Current balance: {balance}")



def transfer(amount, target_account):
    global balance
    if amount > 0 and amount <= balance:
        balance -= amount
        target_account.deposit(amount)
        print(f"Transfer successful! New balance: {balance}")
    else:
        print("Transfer amount must be positive and less than or equal to the balance.")




def main():

    while True:
        print("\nWelcome to the Banking System!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == '2':
            amount = float(input('Enter amount to withdraw: '))
            withdraw(amount)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            amount = float(input('Enter amount to transfer: '))
            target_account = input('Enter target account (for simplicity, we will use the same banking system): ')
            transfer(amount, target_account)

        elif choice == '5':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



