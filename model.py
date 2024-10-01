
class Account:
    def __init__(self, accountNumber, clientId, clientName, accountBalance):
        self.accountNumber = accountNumber
        self.clientId = clientId
        self.clientName = clientName
        self.accountBalance = accountBalance

    def depositMoney(self, amount):
        deduction = 0.19 * amount
        self.accountBalance += (amount - deduction)

    def withdrawMoney(self, amount):
        if(self.accountBalance >= amount):
            self.accountBalance -= amount
            return True
        
        else:
            return False

accounts = []