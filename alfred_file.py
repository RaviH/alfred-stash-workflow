import json
import logging
import os


# Get the full path to your workflow's data directory.
def get_workflow_data_dir():
    data_dir = os.getenv('alfred_workflow_data')
    if data_dir is not None:
        data_dir = data_dir.rstrip('\n')
    else:
        data_dir = "/tmp"

    logging.info("Workflow data directory: %s", data_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir


class AlfredFile:
    def __init__(self, directory_path, file_name):
        self.directory_path = directory_path
        self.file_name = file_name

    # Returns the full path to the file name for your workflow.
    def get_file_name(self):
        file_name = "{0}/{1}".format(self.directory_path, self.file_name)
        logging.info("Full path to file is: %s", file_name)
        return file_name

    # Returns file in write mode
    def get_file_in_write_mode(self):
        return open(self.get_file_name(), 'w+')

    # Writes the dictionary to file.
    def write_to_file(self, in_dict):
        alfred_file = self.get_file_in_write_mode()
        json.dump(in_dict, alfred_file, sort_keys=True, indent=4, separators=(',', ': '))
        logging.info("Alfred file: {0}".format(alfred_file.name))
        return alfred_file

    # Returns the contents of the file as Json and returns a dictionary object.
    def read_json_file(self):
        config_file_name = self.get_file_name()
        if os.path.exists(config_file_name):
            config_file = open(config_file_name, 'r')
            return config_file.read()
        else:
            return {}
