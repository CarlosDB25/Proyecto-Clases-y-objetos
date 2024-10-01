
def createAccount():
    accountNumber = int(input("Ingrese numero de la cuenta: "))
    clientId = int(input("Ingrese su numero de identificacion: "))
    clientName = input("Ingrese su nombre: ")
    accountBalance = float(input("Ingrese saldo actual de la cuenta: "))

    return accountNumber, clientId, clientName, accountBalance

def showAccount(account):
    if(account is not None):
        print(
        f"Numero de cuenta: {account.accountNumber}\n"
        f"Numero de identificacion: {account.clientId}\n"
        f"Nombre del propietario: {account.clientName}\n"
        f"Saldo actual: {account.accountBalance}\n")

    else:
        print("Cuenta invalida")

def getAccountNumber():
    return int(input("Ingrese el numero de su cuenta: "))

def getAmount():
    return float(input("Ingrese la cantidad de dinero: "))

def taskResult(result):
    if(result):
        print("Accion realizada exitosamente.")

    else:
        print("No es posible realizar la accion.")

def menu():
    option = int(input(
        "1. Crear cuenta bancaria\n"
        "2. Mostrar cuentabancaria\n"
        "3. Depositar dinero\n"
        "4. Retirar dinero\n"
        "5. Salir\n\n"
        "Opcion: "
    ))

    return option