import sys
import cmath
import math

# Получаем коэффициенты при х
def get_float(msg, allow_zero):
	x = None
	while x is None:
		try:
			x = float(input(msg))
			if x.is_integer():
				x = int(x)
			if not allow_zero and abs(x) < sys.float_info.epsilon:
				print("Zero isn`t allowed")
				x = None
		except ValueError as err:
			print(err)
	return x


# Определим функцию, возвращающую корни ур-я. Если корень один, второй корень None
def ger_roots(a, b, c):
	x1 = None
	x2 = None
	discr = (b ** 2) - (4 * a * c)
	if discr == 0:
		x1 = -(b / (2 * a))
	else:
		if discr > 0:
			discr_root = math.sqrt(discr)
		else:
			discr_root = cmath.sqrt(discr)
		x1 = (-b + discr_root) / (2 * a)
		x2 = (-b - discr_root) / (2 * a)
	x1_x2 = (x1, x2)
	return x1_x2

	
print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

roots = ger_roots(a, b, c)
equation = (f"{a}x\N{SUPERSCRIPT TWO}{b:+}x{c:+}=0"
f" \N{RIGHTWARDS ARROW} x = {roots[0]:.2}")
if roots[1] is not None:
	equation += f" or x = {roots[1]:.2}"
print(equation)
