class Union:
    def __init__(self, key):
        self.key = key
        self.fee = 0

    def __str__(self):
        return 'Sindicalista numero {}'.format(self.key)