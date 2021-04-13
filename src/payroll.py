from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned
from os import system

clear = lambda: system('clear')
deletedIds = []
lastId = 0

def getId():
    global lastId
    lastId += 1
    return lastId

def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(3) - Estatisticas de funcionários")
    print("(4) - Encontrar Funcionário")
    print("(0) - Sair")
    ans = input()
    return int(ans)

def employeeChoose():
    clear()
    print("Escolha uma opção:")
    print("(1) - Horista")
    print("(2) - Assalariado")
    print("(3) - Comissionado")
    print("(0) - Sair")
    ans = input()
    return int(ans)

def insertHourly():
    #e2 = Hourly('ze', "friburgo", 500, 1.04)
    clear()
    print("Adição de funcionário Horista:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Hourly(name, address, salary)
    clear()
    return employee

def insertSalaried():
#e3 = Salaried('figo', "porto", 5000)
    clear()
    print("Adição de funcionário assalariado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Salaried(name, address, salary)
    clear()
    return employee

def insertComissioned():
    # e4 = Comissioned("tiao", "mcz", 2000, 140)
    clear()
    print("Adição de funcionário comissionado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    bonus = float(input("Digite o bônus: "))
    employee = Comissioned(name, address, salary, bonus)
    clear()
    return employee

def addEmployee():
    employeeAns = employeeChoose()

    if employeeAns == 1:
       employee = insertHourly()
    elif employeeAns == 2:
        employee = insertSalaried()
    elif employeeAns == 3:
        employee = insertComissioned()
    else:
        print("Saindo...")
        exit
    
    return employee

def removeEmployee():
    clear()
    print("Desculpe, ainda não foi implementado :)")
    exit

def employeeStats(dictionary):
    clear()
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 funcionário(a).\n")
    else:
        print("A folha de pagamento contém %d funcionários(as).\n" %len(dictionary))

def findEmployee(dictionary):
    key = int(input("Digite o ID do funcionário: "))
    print("------------------------------")
    print(dictionary[key])
    print("------------------------------")
            


def main():
    employeeDict = {}
    

    while True:
        menuoption = menu()
        if menuoption == 1:
            value = getId()
            employeeDict[value] = addEmployee()
        elif menuoption == 2:
            removeEmployee()
        elif menuoption == 3:
            employeeStats(employeeDict)
        elif menuoption == 4:
            findEmployee(employeeDict)#notimplemented
        else:
            print("Saindo...")
            break

    # clearScreen()
    # print(employeeDict[1])

main()

# e1 = Employee('jao', "madureira")
#e2 = Hourly('ze', "friburgo", 500, 1.04)
#e3 = Salaried('figo', "porto", 5000)
# e4 = Comissioned("tiao", "mcz", 2000, 140)

# print(e4)
#print(e4.bonus)

    
