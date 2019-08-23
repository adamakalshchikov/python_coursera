from .pin import NumerationSystemImitator


class PinCompleter(NumerationSystemImitator):
    def __init__(self, pin_code: str):
        super(PinCompleter, self).__init__(pin_code)
        self.create_generator()
        self.pin_code_length = len(self.suspected_pin)
        self.__iterable_byte = 0

    # Метод в бесконечном цикле перебирает значения младшего разряда
    # Если поднимается StopIteration, атрибут self.__stop_iteration_occurred = True
    def iterate_byte(self):
        try:
            if self.__iterable_byte == 0:
                while True:
                    self.save_variant()
                    self.get_next_value(self.__iterable_byte)
            else:
                self.save_variant()
                self.get_next_value(self.__iterable_byte)
                self.__iterable_byte = 0
        except StopIteration:
            if self.__iterable_byte == self.pin_code_length - 1:
                raise IndexError
            self.restore_generator(self.__iterable_byte)
            self.__iterable_byte += 1
            self.iterate_byte()
