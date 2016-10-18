from __future__ import print_function

import json
import os
import logging
import re

from alfred_config import create_config

bundle_id = "org.javawithravi.alfred.workflow"
base_url_regex = "b.*"
username_regex = "u.*"
password_regex = "p.*"

items_dict = {"items": [
    {
        "title": "base url",
        "subtitle": "base url",
        "arg": "baseUrl",
        "autocomplete": "baseUrl",
    },
    {
        "title": "username",
        "subtitle": "username",
        "arg": "username",
        "autocomplete": "username",
    },
    {
        "title": "password",
        "subtitle": "password",
        "arg": "password",
        "autocomplete": "password",
    }
]}


def execute(query):
    logging.info("query: {0}".format(query))
    words = query.split()

    validate = validate_input(words)
    if validate is None:
        if len(words) < 2:
            print(matching_items(words))
        else:
            command = words[0]
            value = words[1]

            if value is None:
                print(matching_items(words))
            if re.match(base_url_regex, command):
                create_base_url(value)
                print(matching_items(words))
            elif re.match(password_regex, command):
                create_password(value)
                print(matching_items(words))
            else:
                create_username(value)
                print(matching_items(words))
    else:
        print(validate)


def validate_input(words):
    if len(words) == 0:
        items_json = json.dumps(items_dict, sort_keys=True, indent=4, separators=(',', ': '))
        return items_json
    # else:
    #     if len(words) < 2 or words[1] is None:
    #         return foo(words)
    return None


def matching_items(words):
    matches = [x for x in items_dict['items'] if fulfills_some_condition(x, words[0])]
    filtered_items_dict = {'items': matches}
    items_json = json.dumps(filtered_items_dict, sort_keys=True, indent=4, separators=(',', ': '))
    return items_json


def fulfills_some_condition(item, word):
    regex = "{0}.*".format(word)
    found = re.match(regex, item['autocomplete'])
    return found


def create_base_url(base_url):
    create_config('base_url', base_url)


def create_password(password):
    # type: (object) -> object
    create_config('password', password, True)


def create_username(username):
    create_config('username', username)


if __name__ == '__main__':
    os.environ['alfred_workflow_data'] = '/tmp'
    execute('baseUrl http://stash.dev-charter.net/stash/projects')
