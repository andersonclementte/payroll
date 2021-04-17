from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned
from employees.salesReport import SalesReport
from union.union import Union
from os import system

#new branch hello world

clear = lambda: system('clear')
deletedIds = []
lastId = 0
unionID = 0

def getId():
    if (len(deletedIds) > 0):
        return deletedIds.pop(0) #return first item in list and deletes it
    else:
        global lastId
        lastId += 1
        return lastId

def getUnionId():
    global unionID
    unionID += 1
    return lastId

def menu():
    print("Escolha uma opção:")
    print("(1) - Adicionar Funcionário")
    print("(2) - Remover Funcionário")
    print("(3) - Exibir quantidade de funcionários cadastrados")
    print("(4) - Encontrar Funcionário por ID")
    print("(5) - Adicionar ao sindicato")
    print("(6) - Lançar cartão de ponto")
    print("(7) - Lançar resultado de vendas")
    print("(8) - Ver resultado de venda")
    print("(9) - Lançar taxa de serviço")
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
    print("Registro de funcionário Horista:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Hourly(name, address, salary)
    clear()

    return employee

def insertSalaried():
#e3 = Salaried('figo', "porto", 5000)
    clear()
    print("Registro de funcionário assalariado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    employee = Salaried(name, address, salary)
    clear()

    return employee

def insertComissioned():
    # e4 = Comissioned("tiao", "mcz", 2000, 140)
    clear()
    print("Regitro de funcionário comissionado:")
    name = input("Digite o nome: ")
    address = input("Digite o endereço: ")
    salary = float(input("Digite o salario: "))
    bonus = float(input("Digite o bônus: "))
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
        name = dictionary[key]['worker'].name
        deletedIds.append(key)
        del dictionary[key]
        print("Operação bem sucedida, funcionário {} deletado.".format(name))
        return dictionary

def employeeStats(dictionary):
    clear()
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 funcionário(a).\n")
    else:
        print("A folha de pagamento contém %d funcionários(as).\n" %len(dictionary))

def findEmployee(dictionary, uniondict):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("ID inválida.")
    else:
        print("------------------------------")
        print(dictionary[key]['worker'])
        if (dictionary[key]['worker'].kind == 'Comissionado'):
            print("Sales report: {}".format(len(dictionary[key]['sales'])))
        if ('unionKey' in dictionary[key]):
            print("Empregado sindicalizado.")
            print(uniondict[ dictionary[key]['unionKey'] ])
        print("------------------------------")

def unionStatus(dictUnion):
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictUnion):
        print("ID inválida.")
    else:
        print("------------------------------")
        print(dictUnion[key])
        print("------------------------------")

def globalParameters():
    clear()
    print("Id deletadas: {}".format(deletedIds))
    #print(deletedIds)
    print("Proxima id livre: {}".format(lastId+1))

def sendTimeCard(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
        #return
    elif (dictionary[key]['worker'].kind != "Horista"):
        print("Id inválida, funcionário não horista.")
        print("-------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        hours = float(input("Digite as horas trabalhadas: "))
        dictionary[key]['worker'].TimeCard(hours)
        print("Cartão submetido com sucesso.")
        print("-----------------------------")

def sendSalesReport(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
        #return

    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Id inválida, funcionário não comissionado.")
        print("------------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        dateTime = input("Digite a data: ")
        value = float(input("Digite o valor: "))
        saleReport = SalesReport(dateTime, value)
        dictionary[key]['sales'].append(saleReport)
        print("Resultado de vendas submetido com sucesso.")
        print("------------------------------------------")
    
def showSaleReport(dictionary):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
        return
    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Id inválida, funcionário não comissionado.")
        print("------------------------------------------")
    else:
        print("Funcionário:",format(dictionary[key]['worker'].name))
        print("Resultados de vendas: %d" %len(dictionary[key]['sales']))
        print("Ultimo resultado de venda: ")
        print(dictionary[key]['sales'][-1])
        print("--------------------------")

def addToUnion(dictionary, unionDic):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
    else:
        if ('unionKey' in dictionary[key]):
            print("Funcionário já sindicalizado.")
        else:
            unionId = getUnionId()
            dictionary[key]['unionKey'] = unionId
            unionDic[unionId] = Union(unionId)
            print("Funcionario filiado ao sindicado. ID  sindical número {}". format(unionID))


def sendUnionFee(dictionary, unionDic):
    clear()
    key = int(input("Digite o Id do funcionario: "))
    if (key not in dictionary):
        print("ID inválida.")
        print("------------------------------")
    else:
        if ('unionKey' not in dictionary[key]):
            print("Empregado não sindicalizado.")
        else:
            print("Id sindical: %d" %dictionary[key]['unionKey'])
            value = float(input("Digite o valor da taxa:"))
            unionDic[dictionary[key]['unionKey']].incrementFee(value)
            print("Taxa adicionada com sucesso.")




def main():
    employeeDict = {}
    unionDict = {}


    while True:
        menuoption = menu()
        
        if menuoption == 1:
            individualDict = {}
            value = getId()
            employeeOption = employeeChoose()
            if (employeeOption != 0):

                if (employeeOption == 3):
                    individualDict['sales'] = []
                
                individualDict['worker'] = addEmployee(employeeOption)
                
                    
                unionOption = input("Deseja entrar no sindicato? (S/N)")
                if (unionOption == 's' or unionOption == 'S'):
                    unionId = getUnionId()
                    individualDict['unionKey'] = unionId
                    unionDict[unionId] = Union(unionId)
                    print("Funcionario filiado ao sindicado. ID sindical numero {}". format(unionID))
                else:
                    print("Funcionário não filiado ao sindicato.")

                employeeDict[value] = individualDict
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
            findEmployee(employeeDict, unionDict)

        elif menuoption == 5:
            addToUnion(employeeDict, unionDict)

        elif menuoption == 6:
            if (len(employeeDict) > 0):
                sendTimeCard(employeeDict)
            else:
                print("A folha de pagamento está vazia")
                print("------------------------------")

        elif menuoption == 7:
            if (len(employeeDict) > 0):
                sendSalesReport(employeeDict)
            else:
                print("A folha de pagamento está vazia")
                print("------------------------------")
        
        elif menuoption == 8:
            showSaleReport(employeeDict)

        elif menuoption == 9:
            sendUnionFee(employeeDict, unionDict)

        else:
            print("Saindo...")
            break
    

   
main()