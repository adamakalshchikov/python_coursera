import argparse
import json
from pathlib import Path
import os
from shutil import copyfile


FW_PATH = r'C:\FirmwareUpdater\settings.json'
MAIN_PATH = r'\\cri-files\Build\Platforn2.5'
BRANCH_PATH = r'\branch'


def fw_params():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--model', type=int, default=None)
	parser.add_argument('-b', '--build', type=int, default=None)
	parser.add_argument('-br', '--branch', action='store_true', default=False)
	parser.add_argument('-p', '--port', type=int, default=None)
	parser.add_argument('-r','--release', action='store_true', default=False,
						help='Either to update to build`s release version')
	args = parser.parse_args()
	return args


def con_path(build: int, is_branch: bool):
	build_dir = None
	parent_dir = Path(MAIN_PATH)
	if not is_branch:
		temp = parent_dir / 'container'
		for dir in temp.iterdir():
			if build in dir:
				build_dir = build
	assert build_dir is not None
	return build_dir


upd_options = fw_params()

with open('settings.json', 'r+') as f:
	settings = json.load(f)
	settings['com']['number'] = upd_options.port
	json.dump(settings, f)
	f.close()