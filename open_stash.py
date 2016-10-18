import json
import os


def read_from_file(file_name):
    target = open(file_name, 'r')
    return target.read()


def execute(query):
    """Execute the desired command

    Keyword arguments:
    query   -- The query entered by the user

    """
    data_dir = os.getenv('alfred_workflow_data')
    stash_cache = read_from_file("{0}/stash.cache".format(data_dir))
    words = query.split()
    if len(words) == 0:
        print stash_cache
    else:
        word = words[0]
        stash_cache_dict = json.loads(stash_cache)
        matches = [x for x in stash_cache_dict['items'] if fulfills_some_condition(x, word)]
        items_dict = {'items': matches}
        items_json = json.dumps(items_dict, sort_keys=True, indent=4, separators=(',', ': '))
        print items_json


def fulfills_some_condition(item, word):
    found = word in item['subTitle']
    return found


class OpenStash:
    def __init__(self):
        pass

    @staticmethod
    def main():
        data_dir = os.getenv('alfred_workflow_data')
        print(read_from_file("{0}/stash.cache".format(data_dir)))


if __name__ == "__main__":
    execute("brcm")
