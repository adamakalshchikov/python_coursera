import os.path, argparse, tempfile, json


storage_path = os.path.join(tempfile.gettempdir(), 'storage_data')


def create_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k','--key', help='receipt a name for key-value storage', type=str, default=None)
    parser.add_argument('-v', '--value', help='receipt a value for key-value storage', type=str, default=None)
    return parser

with open(storage_path, 'r+') as f:
    parser = create_arguments()
    args = parser.parse_args()
