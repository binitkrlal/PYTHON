# accounts = {}
# def create_account(account_number):
#     if account_number in accounts:
#             print("Account already exists.")
#     else:
#             accounts[account_number] = 0
#             print(f"Account {account_number} created successfully.")

# def deposit(account_number, amount):
#     if account_number in accounts:
#         accounts[account_number] += amount
#         print(f"Deposited {amount} into account {account_number}.")
#         display_balance(account_number)
#     else:
#         print("Account does not exist.")

# def withdraw(account_number, amount):
#     if account_number in accounts:
#         if accounts[account_number] >= amount:
#             accounts[account_number] -= amount
#             print(f"Withdrew {amount} from account {account_number}.")
#             display_balance(account_number)
#         else:
#             print("Insufficient balance.")
#     else:
#         print("Account does not exist.")

# def display_balance(account_number):
#     if account_number in accounts:
#         print(f"Account {account_number} balance: {accounts[account_number]}")
#     else:
#         print("Account does not exist.")



# while True:
#     print("\nMenu:")
#     print("1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check Balance")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         account_number = input("Enter account number: ")
#         create_account(account_number)
#     elif choice == '2':
#         account_number = input("Enter account number: ")
#         amount = float(input("Enter amount to deposit: "))
#         deposit(account_number, amount)
#     elif choice == '3':
#         account_number = input("Enter account number: ")
#         amount = float(input("Enter amount to withdraw: "))
#         withdraw(account_number, amount)
#     elif choice == '4':
#         account_number = input("Enter account number: ")
#         display_balance(account_number)
#     elif choice == '5':
#         print("Exiting program. Thank you!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


