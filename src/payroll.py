import datetime as dt
from employees.employee import Employee
from employees.hourly import Hourly
from employees.salaried import Salaried, Comissioned
from employees.salesReport import SalesReport
from union.union import Union
from os import system

#global variables and stuff
clear = lambda: system('clear')
deletedIds = []
lastId = 0
unionID = 0
today = dt.datetime(2021,1,1)

#Add employee block
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
    return unionID

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
    print("(10) - Editar funcionário")
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
#add employee end block

#remove employee block
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
#end of remove employee block

#payment method block
def choosePaymentMethod():
    clear()
    print("Escolha uma opção:")
    print("(1) - Deposito em conta")
    print("(2) - Cheque em mãos")
    print("(3) - Cheque pelos correios")
    ans = int(input())
    return ans

def employeeStats(dictionary):
    clear()
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 funcionário(a).\n")
    else:
        print("A folha de pagamento contém %d funcionários(as).\n" %len(dictionary))

def findEmployee(dictionary, uniondict, schedule):
    clear()
    key = int(input("Digite o ID do funcionário: "))
    if (key not in dictionary):
        print("ID inválida.")
    else:
        print("--------------------------------")
        print(dictionary[key]['worker'])
        if (dictionary[key]['worker'].kind == 'Comissionado'):
            print("Sales report: {}".format(len(dictionary[key]['sales'])))
            
        if key in schedule['weekly']:
            print("Funcionário pago semanalmente")
        elif key in schedule['bi-weekly']:
            print("Funcionário pago bi-semanalmente")
        elif key in schedule['monthly']:
            print("Funcionário pago mensalmente")
        print("--------------------------------")

        print("Informações sindicais:")
        if ('unionKey' in dictionary[key]):
            print("Empregado sindicalizado.")
            print(uniondict[ dictionary[key]['unionKey'] ])
        else:
            print("Empregado não sindicalizado.")
        print("--------------------------------")

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

#Edit employee block
def editEmployeeOptions():
    clear()
    print("Escolha uma opção:")
    print("(1) - Editar dados pessoais")
    print("(2) - Editar tipo de funcionário")
    print("(3) - Alterar vinculo sindical")
    print("(4) - Alterar agenda de pagamentos")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

def changePersonalData(dictionary, key):
    newName = input("Digite o novo nome: ")
    newAddress = input("Digite o novo endereço: ")
    newSalary = float(input("Digite o novo salário: "))
    if (dictionary[key]['worker'].kind == 'Horista'):
        dictionary[key]['worker'].EditHourly(newName, newAddress, newSalary)
        print("Funcionário editado com sucesso.")
        print("--------------------------------")

    elif (dictionary[key]['worker'].kind == 'Assalariado'):
        dictionary[key]['worker'].EditSalaried(newName, newAddress, newSalary)
        print("Funcionário editado com sucesso.")
        print("--------------------------------")

    elif (dictionary[key]['worker'].kind == 'Comissionado'):
        newBonus = float(input("Digite o novo bonus: "))
        dictionary[key]['worker'].EditComissioned(newAddress, newAddress, newSalary, newBonus)
        print("Funcionário editado com sucesso.")
        print("--------------------------------")

def changeToHourly(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    editedEmployee = Hourly(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeToSalaried(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    editedEmployee = Salaried(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeToComissioned(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    bonus = float(input("Digite o bônus do funcionário: "))
    editedEmployee = Comissioned(name, address, salary, bonus)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de funcionário editado com sucesso!")
    print(dictionary[key]['worker'])

def changeEmployeeType(dictionary, key):
    if (dictionary[key]['worker'].kind == 'Horista'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Comissionado")
        print("(2) - Assalariado")
        choose = int(input())
        if (choose == 1):
            changeToComissioned(dictionary, key)
        elif (choose == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].kind == 'Assalariado'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Comissionado")
        print("(2) - Horista")
        choose = int(input())
        if (choose == 1):
            changeToComissioned(dictionary, key)
        elif (choose == 2):
            changeToHourly(dictionary, key)
        else:
            print("Cancelando...")
        

    elif (dictionary[key]['worker'].kind == 'Comissionado'):
        print("Escolha o novo tipo para o funcionário: ")
        print("(1) - Horista")
        print("(2) - Assalariado")
        choose = int(input())
        if (choose == 1):
            changeToHourly(dictionary, key)
        elif (choose == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando...")

def changeUnionStatus(dictionary, key, unionDic):
    if ('unionKey' in dictionary[key]): 
        unionID = dictionary[key]['unionKey']
        del unionDic[unionID]
        del dictionary[key]['unionKey']
        #print("Funcionário {} foi removido do sindicato".format(dictionary[key]['worker'].name))
        print("Removido do sindicato.")
        
    else:
        unionId = getUnionId()
        dictionary[key]['unionKey'] = unionId
        unionDic[unionId] = Union(unionId)
        print("Funcionario filiado ao sindicado. ID sindical numero {}". format(unionId))

def shedulePaymentOptions():
    clear()
    print("Escolha uma opção:")
    print("(1) - Pagamento semanal")
    print("(2) - Pagamento bi-semanal")
    print("(3) - Pagamento mensal")
    print("(0) - Cancelar")
    ans = int(input())
    return ans

def changePaymentSchedule(option, key, shedule):
    if key in shedule['weekly']:
        shedule['weekly'].remove(key)
    if key in shedule['bi-weekly']:
        shedule['bi-weekly'].remove(key)
    if key in shedule['monthly']:
        shedule['monthly'].remove(key)

    if(option == 1):
        shedule['weekly'].add(key)
    elif (option == 2):
        shedule['bi-weekly'].add(key)
    elif (option == 3):
        shedule['monthly'].add(key)





def editEmployee(dictionary, unionDic, schedule):
    clear()
    print("Atenção, editar um funcionário pode invalidar alguns atributos previamente configurados.")
    res = input("Deseja continuar? (S/n)")
    if (res == 's' or res == 'S'):
        key = int(input("Digite o Id do funcionario: "))
        if (key not in dictionary):
            print("ID inválida.")
            print("------------------------------")
        else:
            option = editEmployeeOptions()
            if (option == 1):
                changePersonalData(dictionary, key)
            elif (option == 2):
                changeEmployeeType(dictionary, key)
            elif (option == 3):
                changeUnionStatus(dictionary, key, unionDic)
            elif (option == 4):
                payoption = shedulePaymentOptions()
                if (payoption > 3):
                    print("Cancelado")
                else:
                    changePaymentSchedule(payoption, key, schedule)
                    print("Agenda alterada com sucesso.")

    else:
        print("Cancelando...")
#end of edit block

def openPayRoll(employeeDict, unionDict, payrollSchedule):
        while True:
            menuoption = menu()
            
            if menuoption == 1:
                individualDict = {}
                value = getId()
                employeeOption = employeeChoose()
                if (employeeOption != 0):
                    newEmployee = addEmployee(employeeOption)

                    if (employeeOption == 1):
                        try:
                            payrollSchedule['weekly'].add(value)
                        except KeyError:
                            payrollSchedule['weekly'] = {value}

                    if (employeeOption == 2):
                        try:
                            payrollSchedule['monthly'].add(value)
                        except KeyError:
                            payrollSchedule['monthly'] = {value}

                    if (employeeOption == 3):
                        try:
                            payrollSchedule['bi-weekly'].add(value)
                        except KeyError:
                            payrollSchedule['bi-weekly'] = {value}
                        individualDict['sales'] = []

                    paymentOption  = choosePaymentMethod()
                    if paymentOption == 1:
                        newEmployee.setPaymentMethod('Deposito em conta')
                    elif paymentOption == 2:
                        newEmployee.setPaymentMethod('Cheque em maos')
                    elif paymentOption == 3:
                        newEmployee.setPaymentMethod('Cheque pelos correios')
                    
                    individualDict['worker'] = newEmployee
                    #individualDict['worker'] = addEmployee(employeeOption)
                    
                        
                    unionOption = input("Deseja entrar no sindicato? (S/N)")
                    if (unionOption == 's' or unionOption == 'S'):
                        unionId = getUnionId()
                        individualDict['unionKey'] = unionId
                        unionDict[unionId] = Union(unionId)
                        print("Funcionario filiado ao sindicado. ID sindical numero {}". format(unionId))
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
                findEmployee(employeeDict, unionDict, payrollSchedule)

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

            elif menuoption == 10:
                editEmployee(employeeDict, unionDict, payrollSchedule)

            else:
                print("Saindo...")
                break

#runs the payments begin:
def runPayRoll(employeeDict, unionDict):
    global today

def main():
    employeeDict = {}
    unionDict = {}
    payrollSchedule = {}
    payrollSchedule['weekly'] = set()
    payrollSchedule['bi-weekly'] = set()
    payrollSchedule['monthly'] = set()

    openPayRoll(employeeDict, unionDict, payrollSchedule)
    # date1 = dt.datetime(2020,4,4)
    # date2 = dt.datetime(2021,5,23)

    # k1 = Hourly("Rafa", "Matao", 500)
    # k1.PaymentVoucher(date1)
    # k1.PaymentVoucher(date2)
    #k1.PrintLastPaymentVoucher()


    
    

   
main()