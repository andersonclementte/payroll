from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def __init__(self, name, address, kind):
        self.name = name
        self.id = id(self)
        self.address = address
        self.kind = kind

    def companyEmail(self):
        return '{}@company.com'.format(self.name)
    
    def __str__(self):
        return 'Nome: {}\nEndereco: {}\nTipo de funcionario: {}\nId: {}'.format(self.name, self.address, self.kind, self.id)