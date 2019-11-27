

class Value:

    def __init__(self, tax = None):
        self.tax = tax

    def __get__(self, instance, owner):
        return self.tax

    def __set__(self, instance, value):
        self.tax = value - instance.commission * value
        return self.tax


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = float(commission)

