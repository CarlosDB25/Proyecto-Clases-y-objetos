from MODELO import model
from UI import ui

def searchAccount(accountNumber):
    for account in model.accounts:
        if account.accountNumber == accountNumber:
            return account
    return None

def getAccount():
    accountNumber = ui.getAccountNumber()

    return searchAccount(accountNumber)

def main():

    while(True):
        
        option = ui.menu()

        if((option > 4) or (option < 1)):
            break

        if(option == 1):
            accountNumber, clientId, clientName, accountBalance = ui.createAccount()
            account = model.Account(accountNumber, clientId, clientName, accountBalance)

            model.accounts.append(account)
            continue

        if(option == 2):
            account = getAccount()

            ui.showAccount(account)
            continue

        if(option == 3):
            account = getAccount()
            amount = ui.getAmount()

            model.Account.depositMoney(account, amount)
            ui.taskResult(True)
            continue

        if(option == 4):
            account = getAccount()
            amount = ui.getAmount()

            ui.taskResult(model.Account.withdrawMoney(account, amount))
            continue


if __name__ == "__main__":
    main()
