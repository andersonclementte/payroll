from employees.employee import Employee

class Salaried(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Assalariado"
        self._salary = salary
    
    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}'.format(self.kind)
    
    


class Comissioned(Salaried):
    def __init__(self, name, address, salary, bonus):
        super().__init__(name, address, salary)
        self.kind = "Comissionado"
        self._bonus = bonus

    def __str__(self):
        return super().__str__()

# g1 = Comissioned("carlos", "Colina", 4000, 500)
# print(g1)