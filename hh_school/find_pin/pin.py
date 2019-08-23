from recordclass import recordclass


class NumerationSystemImitator(object):
    DigitGenerator = recordclass('DigitGenerator', ['bit_generator', 'bit_value'])
    NEIGHBOURHOODS = {
        "1": ['1', "2", "4"],
        "2": ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['8', '6', '9'],
        '0': ['0', '8']
    }

    # Инициализируем экземпляр с предполагаемым пином
    def __init__(self, pin: str):
        if not pin.isnumeric():
            raise ValueError('pin must be numeric')
        self.suspected_pin = pin
        self.__various_of_pin = list()
        self.__digit_handler = dict()

    # Метод добавляет вариант пин-кода в результат (self.__various_of_pin)
    def save_variant(self):
        tmp = list()
        for ind in range(len(self.__digit_handler) - 1, -1, -1):
            tmp.append(self.__digit_handler[ind].bit_value)
        self.__various_of_pin.append("".join(tmp))

    # Метод итерирует генератор, устанавливает следуещее значение в кортеже, нахожящимся в  self.__digit_handler
    # позиция цифры считается с конца числа, начиная с нуля
    def get_next_value(self, position):
        self.__digit_handler[position].bit_value = next(self.__digit_handler[position].bit_generator)

    # Метод восстанавливает генератор, позиция цифры считается с конца числа
    # Для выбора нужной последовательности NumerationSystemImitator.NEIGHBOURHOODS используется первоначальный пинкод
    def restore_generator(self, position):
        seq_key = self.suspected_pin[::-1][position]
        self.__digit_handler[position].bit_generator = (value for value in NumerationSystemImitator.NEIGHBOURHOODS[seq_key])
        self.get_next_value(position)

    # Метод создаёт генераторы для каждой цифры в пинкоде. Разряды считаются с конца числа
    def create_generator(self):
        for n, num in enumerate(reversed(self.suspected_pin)):
            gen = (value for value in NumerationSystemImitator.NEIGHBOURHOODS[num])
            bit_value = next(gen)
            bit_tuple = NumerationSystemImitator.DigitGenerator(gen, bit_value)
            self.__digit_handler[n] = bit_tuple


if __name__ == "__main__":
    pass
