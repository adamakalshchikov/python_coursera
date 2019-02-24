def get_integer(message, name="integer", default=None, minimum=0,
				maximum=100, allow_zero=True):
	class RangeError(Exception):
		pass

	message += ": " if default is None else " [{0}]: ".format(default)
	while True:
		try:
			line = input(message)
			if not line and default is not None:
				return default
			i = int(line)
			if i == 0:
				if allow_zero:
					return i
				else:
					raise RangeError("{0} may not be 0".format(name))
			if not (minimum <= i <= maximum):
				raise RangeError("{name} must be between {minimum} "
								 "and {maximum} inclusive{0}".format(
					" (or 0)" if allow_zero else "", **locals()))
			return i
		except RangeError as err:
			print("ERROR", err)
		except ValueError as err:
			print("ERROR {0} must be an integer".format(name))


def get_string(message, name="string", default=None,
			   minimum_length=0, maximum_length=80):
	message += ": " if default is None else " [{0}]: ".format(default)
	while True:
		try:
			line = input(message)
			if not line:
				if default is not None:
					return default
				if minimum_length == 0:
					return ""
				else:
					raise ValueError("{0} may not be empty".format(
						name))
			if not (minimum_length <= len(line) <= maximum_length):
				raise ValueError("{name} must have at least "
								 "{minimum_length} and at most "
								 "{maximum_length} characters".format(
					**locals()))
			return line
		except ValueError as err:
			print("ERROR", err)