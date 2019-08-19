class PinCompleter(object):
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
        self.digit_generator = list()
        self.__digit_handler = list()

    # Метод добавляет вариант пин-кода в строку-результат
    def flush_variant(self):
        variant = "".join(self.__digit_handler)
        self.__digit_handler.clear()
        self.__various_of_pin.append(variant)

    def add_digit(self, digit):
        self.__digit_handler.append(digit)

    # Метод создаёт генераторы для каждой цифры в пинкоде
    def create_generator(self):
        for num in self.suspected_pin:
            self.digit_generator.append((num_gen for num_gen in PinCompleter.NEIGHBOURHOODS[num]))

    def get_variants(self):
        for d in self.digit_generator:
            self.add_digit(next(d))


def main():
    pass


if __name__ == "__main__":
    main()