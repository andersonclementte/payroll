class Union:
    def __init__(self, key):
        self.key = key
        self.fee = float(50.00)

    def incrementFee(self, increment):
        self.fee += increment

    def __str__(self):
        return 'Sindicalista numero {}\nTaxa sindical: R${}'.format(self.key, self.fee)