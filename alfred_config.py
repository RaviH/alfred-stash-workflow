from __future__ import print_function

import os
import json
from alfred_file import AlfredFile, get_workflow_data_dir
import base64

config_file = AlfredFile(get_workflow_data_dir(), 'config.json')
config_set_error = "Error occurred while setting config for {0}: {1}"


# Returns config file in write mode
def get_config_file_in_write_mode():
    return open(config_file.get_file_name(), 'w+')


# Writes the config dictionary to config file.
def write_to_config_file(config_dict):
    config_file.write_to_file(config_dict)


# Returns the configuration for the workflow in dictionary format
def read_all_configs():
    return json.loads(config_file.read_json_file())


# Create config and store it in config.json file.
def create_config(config_key, config_value, encode=False):
    try:
        config_dict = read_all_configs()
        if encode:
            config_value = base64.b64encode(config_value)
        config_dict[config_key] = config_value
        write_to_config_file(config_dict)
    except Exception as e:
        print(config_set_error.format(config_key, e))


# Returns the config for the given key
def read_config(config_key, decode=False):
    config_dict = json.loads(config_file.read_json_file())
    if config_dict and config_key in config_dict:
        return get_config_value(config_dict, config_key, decode)
    else:
        return None


# Returns decoded value if decode is True, else returns config value as is
def get_config_value(config_dict, config_key, decode):
    config_value = config_dict[config_key]
    if decode:
        config_value = base64.b64decode(config_value)
    return config_value


if __name__ == '__main__':
    os.environ[
        'alfred_workflow_data'] = '/Users/rhasija/Google Drive/Alfred/Alfred.alfredpreferences/workflows/user.workflow.B865A65B-5916-46CE-AE15-D413FFB64F64'
    read_config()
