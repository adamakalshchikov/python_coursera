import doctest


class Transaction:
    """
    >>> t = Transaction(100, "2008-12-09")
    >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
    (100, 'USD', 1.0, 100.0)

    >>> t = Transaction(95000, "2019-05-11", currency="RUB", usd_conversion_rate=1/65.12)
    >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
    (95000, 'RUB', 0.015356265356265355, 1458.8452088452086)
    """
    def __init__(self, amount, date, currency="USD", usd_conversion_rate=1.0,
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
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = None
        self.__all_usd = True
