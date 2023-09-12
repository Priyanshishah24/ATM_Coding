import time

print("Please insert your card.")
time.sleep(5)

password = 1234
pin = int(input("Enter your ATM pin: "))
balance = 10000
max_attempts = 3
attempt_count = 0

if pin == password:
    while True:
        print("""
            1 == Balance
            2 == Withdraw Amount
            3 == Deposit Amount
            4 == Exit
            """
        )
        try:
            option = int(input("Please Enter Your Choice: "))
        except ValueError:
            print("Please Enter a Valid Option")

        if option == 1:
            print(f"Your Bank Account Balance is {balance}")

        elif option == 2:
            if attempt_count >= max_attempts:
                print("Maximum number of attempts reached. Your account has been locked.")
                break

            withdraw_amount = int(input("Please Enter Withdraw Amount: "))

            if withdraw_amount > balance:
                print("Insufficient balance. Please try again.")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your Account")
                print(f"Your Current Balance is {balance}")

        elif option == 3:
            deposit_amount = int(input("Please Enter Deposit Amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your Updated Balance is {balance}")

        elif option == 4:
            break

        else:
            print("Invalid choice. Please try again.")

        if option == 2 and withdraw_amount > balance:
            attempt_count += 1
            print(f"Invalid withdrawal attempt {attempt_count}/{max_attempts}")

else:
    print("Incorrect Pin")


    
