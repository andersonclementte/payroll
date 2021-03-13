class Employee:
    def __init__(self, name):
        self.name = name
        self.id = id(self)
    
    # def __str__(self):
    #     return f'{self.name}'

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
    employeelist.append(Employee("jao"))
    employeelist.append(Employee("ze"))
    employeelist.append(Employee("chico"))
    for obj in employeelist: 
        print( obj.name, obj.id, sep =' ' ) 

    # removeEmployee(employeelist, 'jao')
    # for obj in employeelist: 
    #     print( obj.name, obj.id, sep =' ' ) 
    
main()
    
