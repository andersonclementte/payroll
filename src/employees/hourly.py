from employees.employee import Employee

class Hourly(Employee):
    workHours = 8
    extraHoursRaise = 1.50

    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.kind = "Horista"
        self._salary = salary
        self.workedHours = float(0.0)
        self.workedExtraHours = float(0.0)

    def TimeCard(self, hours):
        if (hours <= 8):
            self.workedHours += hours
        else:
            self.workedHours += 8
            self.workedExtraHours += (hours - 8) 
    

    def __str__(self):
        return super().__str__() + 'Tipo de empregado: {}\nHoras trabalhadas: {}\nHoras extras trabalhadas: {}'.format(self.kind, self.workedHours, self.workedExtraHours)

# k1 = Hourly("Rafa", "Matao", 500, 1.04)
# print(k1)