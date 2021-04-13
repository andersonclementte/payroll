from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned
from os import system

clear = lambda: system('clear')
deletedIds = []
lastId = 0

def getId():
    if (len(deletedIds) > 0):
        return deletedIds.pop(0) #return first item in list and deletes it
    else:
        global lastId
        lastId += 1
        return lastId

def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(3) - Exibir quantidade de funcionários cadastrados")
    print("(4) - Encontrar Funcionário por ID")
    print("(5) - Exibir Ids deletadas e proxima id")
    print("(6) - Lançar cartão de ponto")
    print("(7) - Lançar resultado de vendas")
    print("(0) - Sair")
    ans = int(input())
    return ans

def employeeChoose():
    clear()
    print("Escolha uma opção:")
    print("(1) - Horista")
    print("(2) - Assalariado")
    print("(3) - Comissionado")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

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
    salary = float(input("Digite o salario:"))
    bonus = float(input("Digite o bônus:"))
    employee = Comissioned(name, address, salary, bonus)
    clear()
    return employee

def addEmployee(option):

    if option == 1:
       employee = insertHourly()
    elif option == 2:
        employee = insertSalaried()
    elif option == 3:
        employee = insertComissioned()
    
    return employee

def removeEmployee(dictionary):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("Id inválida, nenhum funcionário deletado.")
        return dictionary
    else:
        deletedIds.append(key)
        del dictionary[key]
        print("Operação bem sucedida, funcionário deletado.")
        return dictionary

def employeeStats(dictionary):
    clear()
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 funcionário(a).\n")
    else:
        print("A folha de pagamento contém %d funcionários(as).\n" %len(dictionary))

def findEmployee(dictionary):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("ID inválida.")
    else:
        print("------------------------------")
        print(dictionary[key])
        print("------------------------------")

def globalParameters():
    clear()
    print("Id deletadas: {}".format(deletedIds))
    #print(deletedIds)
    print("Proxima id livre: {}".format(lastId+1))

def sendTimeCard(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (dictionary[key].kind != "Horista"):
        print("Id inválida, funcionário não horista.")
        print("-------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key].name))
        hours = float(input("Digite as horas trabalhadas: "))
        dictionary[key].TimeCard(hours)
        print("Cartão submetido com sucesso.")
        print("-----------------------------")

def sendSalesReport(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (dictionary[key].kind != "Comissionado"):
        print("Id inválida, funcionário não comissionado.")
        print("------------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key].name))
        dateTime = input("Digite a data: ")
        value = float(input("Digite o valor: "))
        dictionary[key].SalesReport(dateTime, value)
        print("Resultado de vendas submetido com sucesso.")
        print("------------------------------------------")


def main():
    employeeDict = {}
    

    while True:
        menuoption = menu()
        if menuoption == 1:
            value = getId()
            employeeOption = employeeChoose()
            if (employeeOption != 0):
                employeeDict[value] = addEmployee(employeeOption)
                print("Operação bem sucedida, Id do funcionário: %d" %value)
                print("------------------------------")
            else:
                print("Voltando...")
                print("------------------------------")
        elif menuoption == 2:
            removeEmployee(employeeDict)
        elif menuoption == 3:
            employeeStats(employeeDict)
        elif menuoption == 4:
            findEmployee(employeeDict)
        elif menuoption == 5:
            globalParameters()
        elif menuoption == 6:
            if(len(employeeDict) > 0):
                sendTimeCard(employeeDict)
            else:
                print("A folha de pagamento está vazia")
                print("------------------------------")
        elif menuoption == 7:
            if(len(employeeDict) > 0):
                sendSalesReport(employeeDict)
            else:
                print("A folha de pagamento está vazia")
                print("------------------------------")
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

    
