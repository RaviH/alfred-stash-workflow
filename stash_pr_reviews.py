import base64
import json

import requests

import alfred_config
from alfred_item import Item


def execute(role):
    base_url = alfred_config.get_base_url()
    values = get_query_params(role)
    final_url = "{0}/stash/rest/inbox/latest/pull-requests".format(base_url)
    response = requests.get(final_url, params=values, headers=get_auth_header())

    items_dict = {'items': [
        Item('No PRs for review', 'No PRs for review', 'No PRs for review', 'No PRs for review', 'No PRs for review').__dict__
    ]}

    if response.ok:
        response_json = response.json()
        items = [get_item(value) for value in response_json['values']]
        items_dict = {'items': items}

    print json.dumps(items_dict, sort_keys=True, indent=4, separators=(',', ': '))


def get_item(value):
    url = value['links']['self'][0]['href']
    repo = value['fromRef']['repository']['slug']
    item = Item(repo, repo, url, repo, url)
    return item.__dict__


def get_query_params(role):
    values = {
        'role': role,
        'start': '0',
        'limit': '10',
        'withAttributes': 'true',
        'state': 'OPEN',
        'order': 'oldest'
    }
    return values


def get_auth_header():
    username = alfred_config.get_username()
    password = alfred_config.get_password()
    auth_header = "Basic %s" % base64.encodestring('%s:%s' % (username, password))
    header = {"Authorization": auth_header.rstrip('\n')}
    return header


if __name__ == "__main__":
    execute('author')
