
class Transaction:
    """
    >>> t = Transaction(100, "2008-12-09")
    >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
    (100, 'USD', 1.0, 100.0)

    >>> t = Transaction(95000, "2019-05-11", currency="RUB", usd_conversion_rate=1/65.12)
    >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
    (95000, 'RUB', 0.015356265356265355, 1458.8452088452086)

    >>> t = Transaction(100.15, "2008-12-09")
    >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
    (100.15, 'USD', 1.0, 100.15)
    """
    def __init__(self, amount: (int, float), date, currency="USD", usd_conversion_rate=1.0,
                 description=None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def description(self):
        return self.__description

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def usd(self):
        return self.amount * self.usd_conversion_rate


class Account:
    """

    """
    def __init__(self, number: int, name: str):
        assert len(name) > 3, "account`s name length must be at least 4 characters"
        self.__name = name
        self.__number = number
        self.__transactions = list()

    @property
    def number(self):
        return self.__number

    @property
    def all_usd(self):
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True

    @property
    def balance(self):
        total = 0
        for transaction in self.__transactions:
            total += transaction.usd
        return total

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name) > 3, "account`s name length must be at least 4 characters"
        self.__name = name


if __name__ == "__main__":
    import doctest
    doctest.testmod()
