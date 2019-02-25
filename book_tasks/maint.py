from collections import OrderedDict
import os


def main():
	files = collect_files()
	choise_file(files)


def collect_files():
	"""Функция возвращает лист с файлами с расширением '.lst'	"""

	lst_files = list()
	for file in os.listdir("."):
		if file.endswith(".lst"):
			lst_files.append(file)
	if not lst_files:
		file = create_new_file()
		lst_files.append(file)
	return lst_files


def choise_file(file_list: list):
	"""Функция принимает лист с файлами и возвращает словарь, где ключ- порядковый номер
		 значение - сам файл."""

	d = OrderedDict()
	d = {k: v for k, v in enumerate(file_list, start=1)}
	d[0] = "Create new file"
	return d


def create_new_file():
	msg = "Input name of the new .lst file: "
	filename = input(msg)
	f = open(filename, "w", encoding="utf8")
	f.close()
	return filename




if __name__ == "__main__":
	main()