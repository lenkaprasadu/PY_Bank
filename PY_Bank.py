#simple py bank

#Features
# 1. Deposit money (supports decimal amounts)
# 2. Withdraw money (cannot exceed available balence)
# 3. check current balance
# 4. view transction history
# 5. show total deposits and withdrawals
# 6. menu-based navigation with confirmation messages
# 7. exit option to close the program

balance=0.0
transaction=[]

def depodit(amount):
    global balance
    
    balance=balance+amount
    transaction.append(f'deposit {amount}/-')
    print(f'{amount} deposited successfully\n')


def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficent balance")
    else:
        balance=balance-amount
        transaction.append(f'withdraw {amount}/-')
        print(f'{amount} withdraw successfully\n')


def chackBalance():
    print(f'current balance : {balance}\n')


def transactionHistory():
    if not transactions:
        print("NO transactions.\n")
    else:
        print('-----transaction Histry------')
        for t in transactions:
            print('_',t)
        deposits = sum(1 for t in transactions if "deposit" in t)
        withdraws = sum(1 for t in transactions if "withdraw" in t)
        print(f'\n Total deposits: {deposits} ')
        print(f'\n total withdraws: {withdraws}')
    

def menu():
    while True:
        print("-------PyBank menu--------")
        print("1. deposit")
        print("2. withdraw")
        print("3. chackBalance")
        print('4. view transaction history')
        print("5. exit")
        
        
        choice=input("enter the choice :")
        
        if choice=='1':
            amount = float(input("Enter your amount to depdit :"))
            depodit(amount)
        elif choice =='2':
            amount = float(input("enter your amount to withdraw :"))
            withdraw(amount)
        elif choice =='3':
            chackBalance()
        elif choice =='4':
            transactionhistory()
        elif choice =='5':
            print('Thank you for using pybank. good by')
            break
        else:
            print('invalid choice')
menu()
