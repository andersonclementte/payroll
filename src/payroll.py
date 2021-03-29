from employees.employee import Employee
from employees.hourly import *
from employees.salaried import *


def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(0) - Sair")
    ans = input()
    return int(ans)

def addEmployee(listPar):
    employeeInput = input("Digite o nome do funcionário\n")
    listPar.append(Employee(employeeInput))
    listPar.append(Employee("ze"))
    return listPar

def removeEmployee(listPar, idPar):
    for obj in listPar: 
        if listPar.name == idPar:
            listPar.pop(obj) 
    #return listPar
            


def main():
    employeelist = []
    # menuoption = menu()
    # if menuoption == 1:
    #    employeelist = addEmployee(employeelist)
    # elif menuoption == 2:
    #     removeEmployee()
    # else:
    #     print("Saindo")
    #     exit

    #print(employeelist)
    # employeelist.append(Employee("jao"))
    # employeelist.append(Employee("ze"))
    # employeelist.append(Employee("chico"))
    # for obj in employeelist: 
    #     print( obj.name, obj.id, sep =' ' ) 

    # removeEmployee(employeelist, 'jao')
    # for obj in employeelist: 
    #     print( obj.name, obj.id, sep =' ' ) 
    
e1 = Employee('jao', "madureira", "Horista")
e2 = Hourly('ze', "friburgo", "Horista", 500, 1.04)
e3 = Salaried('figo', "porto", "Assalariad", 5000)
e4 = Comissioned("tiao", "mcz", "Comissionado", 2000, 140)

print(e4)
print(e4.bonus)


    
