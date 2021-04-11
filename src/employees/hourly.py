from employees.employee import Employee

class Hourly(Employee):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Horista"
        self._salary = salary
        self._extraHoursFactor = 1.5

    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}'.format(self.kind)

# k1 = Hourly("Rafa", "Matao", 500, 1.04)
# print(k1)