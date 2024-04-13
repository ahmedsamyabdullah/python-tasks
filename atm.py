account_balance = int(input("Enter your account balance : "))
amount = int(input("Enter the amount you want withdraw : "))
if amount%5 ==0:
    if account_balance>amount:
        account_balance = account_balance - amount - 0.50
        if account_balance > 0:
            print("Done and your account balance = "+ str(account_balance))
        else:
            print("your account balance hasn't enough money")
    else:
        print("please enter amount less than account balance")
else:
    print("this amount not multiple of 5.. try again")