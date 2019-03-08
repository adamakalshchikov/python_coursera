from shutil import copyfile
from itertools import count
from pathlib import Path
import argparse
import json
import sys
import os

FW_PATH = r'C:\FirmwareUpdater'
MAIN_PATH = r'\\cri-files\Build\Platforn2.5'
BRANCH_PATH = r'\branch'


def fw_params():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--model', type=str, default=None)
	parser.add_argument('-b', '--build', type=int, default=None)
	parser.add_argument('-br', '--branch', action='store_true', default=False)
	parser.add_argument('-p', '--port', type=int, default=None)
	parser.add_argument('-r', '--release', action='store_true', default=False,
						help='Установите данный флаг, если требуется установить релизную версию прошивки')
	args = parser.parse_args()
	return args


def get_candidates(build: int, is_branch: bool):
	"""Функция принимает на вход номер билда и сведения о брачне, возвращает словарь с директориями,
	содержащими в названии номер билда."""

	build_dirs = {}
	number = count(start=1)
	parent_dir = Path(MAIN_PATH)
	if not is_branch:
		temp = parent_dir / 'container'
	else:
		branch = input("Укажите бранч, в котором находится контейнер: ")
		temp = parent_dir / f'{branch}' / 'container'
	for directory in temp.iterdir():
		if str(build) in directory.name:
			build_dirs[number] = directory
	assert build_dirs is not None
	return build_dirs


def choose_dir(list_of_directories: list):
	""" Функция принимает лист с папками, содержащими прошивки, номера которых совпадают с искомой и предлагает выбрать
		одну из них
	"""

	if len(list_of_directories) > 1:
		candiates = dict()
		msg = f'Введите номер директории (от 1 до {0})'
		print('Выберете требуемый каталог:')
		for elem in enumerate(list_of_directories, start=1):
			print(f'{elem[0]}. {elem[1]}')
			candiates[str(elem[0])] = elem[1]
	else:
		return list_of_directories[0]
	while True:
		choose = None
		try:
			choose = input(msg.format(len(candiates)))
			return candiates[choose]
		except KeyError:
			response = 'y'
			response = input(f'Введено некорркетное значение: {choose}.\nПовторить попытку ввода?[(y)/n]: ')
			if response.lower() in {'no', 'n'}:
				sys.exit(0)


def file_copier(build_dir: Path, is_release: bool, build: int, model: str):
	"""Функция копирует контейнер с прошивкой в папку FirmwareUpdater, возвращает имя контейнера

		build_dir - корневая директория билда, содержащая папки 'debug' и 'release';
		is_release - если True - выбирается папка 'release';
		build - номер билда, используется для исключения ошибочного выбора папки;
		model - модель прошиваемого оразца ККТ;
	 """

	release_debug_switch = {True: 'release', False: 'debug'}
	with open('models.json') as file:
		models_name = json.load(file)
		try:
			directory_of_container = build_dir / release_debug_switch[is_release] / models_name[model] / 'All'
		except KeyError as err:
			print(err, '\nПроверьте, корректно ли введа модель: ', model)
			sys.exit()
		file.close()
	con_name = None
	for child in directory_of_container.iterdir():
		if str(build) in child:
			copyfile(src=str(child), dst=str(Path(FW_PATH / child.name)))
			con_name = child.name
	return con_name


if __name__ == '__main__':
	upd_options = fw_params()

	# Пишем номер порта в settings.json
	with open(os.path.join(FW_PATH, 'settings.json'), 'r+') as file_settings:
		settings = json.load(file_settings)
		settings['com']['number'] = upd_options.port
		json.dump(settings, file_settings)
		file_settings.close()

	list_of_directories = get_candidates(upd_options.build, upd_options.release)
	dir_with_container = choose_dir()

	container_name = file_copier()
	print(f'FirmwareUpdater.exe -f "{container_name}"')  # использовать для отладки
# os.system(f'FirmwareUpdater.exe -f "{container_name}"')
