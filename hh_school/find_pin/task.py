from pin import NumerationSystemImitator


class PinCompleter(object):
    def __init__(self, pin_code: str):
        self.pin_code = NumerationSystemImitator(pin_code)
        self.pin_code.create_generator()
        self.pin_code_length = len(self.pin_code.suspected_pin)
        self.__iterable_byte = 0

    # Метод в бесконечном цикле перебирает значения младшего разряда
    # Если поднимается StopIteration, атрибут self.__stop_iteration_occurred = True
    def iterate_byte(self):
        try:
            if self.__iterable_byte == 0:
                while True:
                    self.pin_code.save_variant()
                    self.pin_code.get_next_value(self.__iterable_byte)
            else:
                self.pin_code.save_variant()
                self.pin_code.get_next_value(self.__iterable_byte)
                self.__iterable_byte = 0
        except StopIteration:
            if self.__iterable_byte == self.pin_code_length - 1:
                raise IndexError
            self.pin_code.restore_generator(self.__iterable_byte)
            self.__iterable_byte += 1
            self.iterate_byte()
