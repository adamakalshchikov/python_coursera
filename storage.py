import os.path, argparse, tempfile, json


storage_path = os.path.join(tempfile.gettempdir(), 'storage_data')


def create_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k','--key', help='receipt a name for key-value storage', type=str, default=None)
    parser.add_argument('-v', '--value', help='receipt a value for key-value storage', type=str, default=None)
    return parser

def write_to_json(destination, key, value=None):
    with open(destination, 'a') as file_obj:
        json.dump({key: value}, file_obj)
        file_obj.close()


parser = create_arguments()
args = parser.parse_args()
#with open(storage_path, 'r+') as f:
