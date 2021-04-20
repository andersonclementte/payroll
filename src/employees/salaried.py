from employees.employee import Employee

class Salaried(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Assalariado"
        self._salary = salary

    def EditSalaried(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = salary
    
    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}'.format(self.kind)
    
    


class Comissioned(Salaried):
    def __init__(self, name, address, salary, bonus):
        super().__init__(name, address, salary)
        self.kind = "Comissionado"
        self._bonus = bonus
    #     self.date = None
    #     self.value = None

    # def SalesReport(self, date, value):
    #     self.date = date
    #     self.value = value

    def EditComissioned(self, name, address, salary, bonus):
        self.name = name
        self.address = address
        self.salary = salary
        self.bonus = bonus

    def __str__(self):
    #     if (bool(self.date)):
    #         return super().__str__() + 'Resultado de vendas:\nData: {}\nValor {}\n'.format(self.date, self.value)
    #     else:
        return super().__str__()
