from employees.employee import Employee

class Salaried(Employee):
    def __init__(self, name, address, kind, salary):
        super().__init__(name, address, kind)
        self._salary = salary
    
    


class Comissioned(Salaried):
    def __init__(self, name, address, kind, salary, bonus):
        super().__init__(name, address, kind, salary)
        self._bonus = bonus

# g1 = Comissioned("carlos", "Colina", "Comissionado", 4000, 500)
# print(g1.bonus)
# print(g1.name)