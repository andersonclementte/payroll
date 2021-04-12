from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned

keysCache = []
lastId = 0

def getId():
    global lastId
    lastId += 1
    return lastId


def clearScreen():
    print("\n")
    print("\n")
    print("\n")
    print("\n")


def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(0) - Sair")
    ans = input()
    clearScreen()
    return int(ans)

def employeeChoose():
    print("Escolha uma opção:")
    print("(1) - Horista")
    print("(2) - Assalariado")
    print("(3) - Comissionado")
    print("(0) - Sair")
    ans = input()
    clearScreen()
    return int(ans)

#listParameter
def insertHourly():
    #e2 = Hourly('ze', "friburgo", 500, 1.04)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))

    employee = Hourly(name, address, salary)
    return employee

def insertSalaried():
#e3 = Salaried('figo', "porto", 5000)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))

    employee = Salaried(name, address, salary)
    return employee

def insertComissioned():
    # e4 = Comissioned("tiao", "mcz", 2000, 140)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    bonus = float(input("Digite o bônus: "))

    employee = Comissioned(name, address, salary, bonus)
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

def removeEmployee(listPar):
    pass
            


def main():
    employeelist = []
    employeeDict = {}
    value = getId()

    menuoption = menu()

    if menuoption == 1:
        employeeDict[value] = addEmployee()
    elif menuoption == 2:
        removeEmployee()
    else:
        print("Saindo...")
        exit

    clearScreen()
    print(employeeDict[1])
    # employeelist.append(Employee("jao"))
    # employeelist.append(Employee("ze"))
    # employeelist.append(Employee("chico"))
    # for obj in employeelist: 
    #     print( obj.name, obj.id, sep =' ' ) 

    # removeEmployee(employeelist, 'jao')
    # for obj in employeelist: 
    #     print( obj.name, obj.id, sep =' ' ) 

main()

# e1 = Employee('jao', "madureira")
#e2 = Hourly('ze', "friburgo", 500, 1.04)
#e3 = Salaried('figo', "porto", 5000)
# e4 = Comissioned("tiao", "mcz", 2000, 140)

# print(e4)
#print(e4.bonus)

    
