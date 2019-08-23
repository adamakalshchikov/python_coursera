from .pin import NumerationSystemImitator


class PinCompleter(object):
    def __init__(self, pin_code: str):
        self.pin_code = NumerationSystemImitator(pin_code)
        self.pin_code.create_generator()
        self.__stop_iteration_occurred = False

    # Метод в бесконечном цикле перебирает значения младшего разряда
    # Если поднимается StopIteration, атрибут self.__stop_iteration_occurred = True
    def iterate_lowest_byte(self):
        while True:
            try:
                self.pin_code.save_variant()
                self.pin_code.get_next_value(0)
            except StopIteration:
                self.__stop_iteration_occurred = True
                self.pin_code.restore_generator(0)
