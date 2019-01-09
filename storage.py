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


def get_value_by_key(obj_with_json, key_required):
    with open(obj_with_json, 'r') as file_obj:
        data_file = file_obj.read()
        data = json.load(data_file)
        file_obj.close()


parser = create_arguments()
args = parser.parse_args()
if args.value is None:
    get_value_by_key(storage_path, args.key)
else:
    write_to_json(storage_path, args.key, args.value)
