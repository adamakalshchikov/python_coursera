from shutil import copy2
from pathlib import Path
import argparse
import json
import sys
import os

FW_PATH = r'C:\FirmwareUpdater'
MAIN_PATH = r'\\cri-files\Builds$\FRPlatform2.5'
BRANCH_PATH = r'\branch'
OT = r'C:\ProgramData\ATOL\OT'


def fw_params():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--model', type=str, default=None)
	parser.add_argument('-b', '--build', type=int, default=None)
	parser.add_argument('-br', '--branch', action='store_true', default=False,
						help='Установите данный флаг, если прошивка была собрана в бранче. Далее потребуется ввести название бранча.')
	parser.add_argument('-p', '--port', type=int, default=None, help='Порт, к которому подключена ККТ.')
	parser.add_argument('-r', '--release', action='store_true', default=False,
						help='Установите данный флаг, если требуется установить релизную версию прошивки. По умолчанию будет установлена отладочная версия.')
	args = parser.parse_args()
	return args


def get_candidates(build: int, is_branch: bool):
	"""Функция принимает на вход номер билда и сведения о брачне, возвращает словарь с директориями,
	содержащими в названии номер билда."""

	build_dirs = list()
	parent_dir = Path(MAIN_PATH)
	if not is_branch:
		temp = parent_dir / 'container'
	else:
		branch = input("Укажите бранч, в котором находится контейнер: ")
		temp = parent_dir / 'branch' / f'{branch}' / 'container'
	for directory in temp.iterdir():
		if str(build) in directory.name:
			build_dirs.append(directory)
	try:
		assert len(build_dirs) >= 1
	except AssertionError:
		print('Не найдена указанная версия прошивки. Введите номер прошивки, существующий в папке ...\Platforma2.5\container\,либо укажите бранч, в котором находится требуемый билд')
		sys.exit(0)
	return build_dirs


def choose_dir(directories_candidates: list):
	""" Функция принимает лист с папками, содержащими прошивки, номера которых совпадают с искомой и предлагает выбрать
		одну из них
	"""

	if len(directories_candidates) > 1:
		candidates = dict()
		msg = 'Выберете папку с прошивкой (от 1 до {0}): '
		print('Выберете требуемый каталог:')
		for elem in enumerate(directories_candidates, start=1):
			print(f'{elem[0]}. {elem[1]}')
			candidates[str(elem[0])] = elem[1]
	else:
		return directories_candidates[0]
	while True:
		choose = None
		try:
			choose = input(msg.format(len(candidates)))
			return candidates[choose]
		except KeyError:
			response = input(f'Введено некорркетное значение: {choose}.\nПовторить попытку ввода?[(y)/n]: ')
			if response.lower() in {'no', 'n'}:
				sys.exit(0)


def file_copier(build_dir: Path, is_release: bool, build: int, model: str):
	"""	Функция копирует контейнер с прошивкой в папку FirmwareUpdater, возвращает имя контейнера

		build_dir - корневая директория билда, содержащая папки 'debug' и 'release';
		is_release - если True - выбирается папка 'release';
		build - номер билда, используется для исключения ошибочного выбора папки;
		model - модель прошиваемого оразца ККТ;
	"""

	release_debug_switch = {True: 'release', False: 'debug'}
	with open(os.path.join(OT,'models.json')) as file:
		models_name = json.load(file)
		try:
			directory_of_container = build_dir / release_debug_switch[is_release] / models_name[model] / 'All'
		except KeyError as err:
			print(err, '\nПроверьте, корректно ли введа модель: ', model)
			sys.exit()
		file.close()
	con_name = None
	for child in directory_of_container.iterdir():
		if str(build) in child.name:
			copy2(src=str(child), dst=str(Path(FW_PATH) / child.name))
			con_name = child.name
	return con_name


if __name__ == '__main__':
	upd_options = fw_params()
	
	# Пишем номер порта в settings.json
	with open(os.path.join(FW_PATH, 'settings.json'), 'r', encoding='cp1251') as file_settings:
		settings = json.load(file_settings)
		file_settings.close()
	with open(os.path.join(FW_PATH, 'settings.json'), 'w', encoding='cp1251') as file_settings:
		settings['com']['number'] = upd_options.port
		json.dump(settings, file_settings)
		file_settings.close()
		


	list_of_directories = get_candidates(upd_options.build, upd_options.branch)
	dir_with_container = choose_dir(list_of_directories)
	container_name = file_copier(dir_with_container, upd_options.release, upd_options.build, upd_options.model)
	#print(f'FirmwareUpdater.exe -f "{container_name}"')  # использовать для отладки
	os.system('cd C:\FirmwareUpdater')
	os.system(f'C:\FirmwareUpdater\FirmwareUpdater.exe -f "{container_name}"')
