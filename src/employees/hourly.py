from employees.employee import Employee

class Hourly(Employee):
    def __init__(self, name, address, kind, salary, extraHoursFactor):
        super().__init__(name, address, kind)
        self._salary = salary
        self._extraHoursFactor = extraHoursFactor

# k1 = Hourly("Rafa", "Matao", "Trabaio", 500, 1.04)
# print(k1)