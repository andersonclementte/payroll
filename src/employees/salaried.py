from employees.employee import Employee

class Salaried(Employee):
    def __init__(self, name, address, kind, salary):
        super().__init__(name, address, kind)
        self.salary = salary


class Comissioned(Salaried):
    def __init__(self, name, address, kind, salary, bonus):
        super().__init__(self, name, address, kind, salary)
        self.bonus = bonus