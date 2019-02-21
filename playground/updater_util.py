from pathlib import Path
from shutil import copyfile
from itertools import count
import argparse
import json
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
	parser.add_argument('-r','--release', action='store_true', default=False,
						help='Either to load release version')
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
		branch = input("Specify the branch, where container built: ")
		temp = parent_dir / f'{branch}' / 'container'
	for directory in temp.iterdir():
		if build in directory:
			build_dirs[number] = build
	assert build_dirs is not None
	return build_dirs


def


def file_copier(build_dir: Path, is_release: bool, build: int, model: str, dst = FW_PATH):
	"""Функция копирует контейнер с прошивкой в папку FirmwareUpdater

	build_dir - корневая директория билда, содержащая папки 'debug' и 'release';
	is_release - если True - выбирается папка 'release';
	build - номер билда, используется для исключения ошибочного выбора папки;
	model - модель прошиваемого оразца ККТ;
	dst - папка, в которую будет скопирован контейнер
	 """

	dir = build_dir / 'release' if is_release else build_dir / 'debug'
	for d in dir.iterdir():
		# выбор папки по модели ККТ


upd_options = fw_params()

with open(os.path.join(FW_PATH, 'settings.json'), 'r+') as f:
	settings = json.load(f)
	settings['com']['number'] = upd_options.port
	json.dump(settings, f)
	f.close()


os.system(f'FirmwareUpdater.exe -f "{container_name}"')