from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned

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
def insertHourly(listPar):
    #e2 = Hourly('ze', "friburgo", 500, 1.04)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))

    employee = Hourly(name, address, salary)
    listPar.append(employee)
    return listPar

def insertSalaried(listPar):
#e3 = Salaried('figo', "porto", 5000)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))

    employee = Salaried(name, address, salary)
    listPar.append(employee)
    return listPar

def insertComissioned(listPar):
    # e4 = Comissioned("tiao", "mcz", 2000, 140)
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    bonus = float(input("Digite o bônus: "))

    employee = Comissioned(name, address, salary, bonus)
    listPar.append(employee)
    return listPar

def addEmployee(listPar):
    employeeAns = employeeChoose()

    if employeeAns == 1:
       listPar = insertHourly(listPar)
    elif employeeAns == 2:
        listPar = insertSalaried(listPar)
    elif employeeAns == 3:
        listPar = insertComissioned(listPar)
    else:
        print("Saindo...")
        exit
    
    return listPar

def removeEmployee(listPar, idPar):
    pass
            


def main():
    employeelist = []
    menuoption = menu()
    if menuoption == 1:
       employeelist = addEmployee(employeelist)
    elif menuoption == 2:
        removeEmployee()
    else:
        print("Saindo...")
        exit

    clearScreen()
    print(employeelist[0])
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

    
