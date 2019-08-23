from collections import namedtuple


class PinCompleter(object):
    DigitGenerator = namedtuple('DigitGenerator', ['bit_generator', 'bit_value'])
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
            tmp.append(self.__digit_handler[ind][1])
        self.__various_of_pin.append("".join(tmp))

    # Метод итерирует генератор, устанавливает следуещее значение в кортеже, нахожящимся в  self.__digit_handler
    # позиция цифры считается с конца числа, начиная с нуля
    def get_next_value(self, position):
        self.__digit_handler[position][1] = next(self.__digit_handler[position][0])

    # Метод создаёт генераторы для каждой цифры в пинкоде. Разряды считаются с конца числа
    def create_generator(self):
        for n, num in enumerate(reversed(self.suspected_pin)):
            gen = (value for value in PinCompleter.NEIGHBOURHOODS[num])
            bit_value = next(gen)
            bit_tuple = PinCompleter.DigitGenerator(gen, bit_value)
            self.__digit_handler[n] = bit_tuple


def main():
    pass


if __name__ == "__main__":
    main()
