print("Welcome to Chase bank.")
print("Have a nice day!")

def user_request():
    req = input("Your current balance is \n 4000 \n What would you like to do? \n deposit, withdraw, check_balance ")
    if req == "balance":
        print('Your balance is 4000')
    elif req == "withdraw":
        withdraw_amount = input("How much would you like to withdraw? ")
        new_balance = 4000 - float(withdraw_amount)
        print(f"Your new balance is {new_balance}")
    else: 
        deposit_amount = input("How much are you depositing today? ")
        new_balance = 4000 + float(deposit_amount)
        print(f"Your new balance is {new_balance}")

print(user_request())
