# author Ravi Hasija


import os
import json
import stashy
import asgard_item
import find_credentials
import alfred_config

os.environ['alfred_workflow_data'] = '/Users/rhasija/Library/Application Support/Alfred 3/Workflow Data/org.javawithravi.alfred.workflow.stash'


def connect_to_stash():
    account = find_credentials.get_username()
    password = find_credentials.get_password()
    base_url = alfred_config.read_config('base_url')
    return stashy.connect("{0}/stash".format(base_url), account, password)


def get_items():
    stash = connect_to_stash()
    project_list = stash.projects.list()
    items = []
    for project in project_list:
        project_key = project['key']
        repo_list = stash.projects[project_key].repos.list()
        for repo in repo_list:
            repo_name = repo['slug']
            uid = project_key + ":" + repo_name
            title = project_key + '::' + repo_name
            url = repo['links']['self'][0]['href']
            arg = url
            auto_complete = repo_name
            item = asgard_item.Item(uid, title, arg, auto_complete, url)
            items.append(item.__dict__)
    return items


def write_to_file(file_name, items):
    target = open(file_name, 'w+')
    target.truncate()
    target.write(items)


def execute():
    items = get_items()
    print items
    items_json = json.dumps({'items': items}, sort_keys=True, indent=4, separators=(',', ': '))
    data_dir = os.getenv('alfred_workflow_data')
    write_to_file("{0}/stash.cache".format(data_dir), items_json)
    result = {'result': 'successful'}
    print(json.dumps(result))


if __name__ == "__main__":
    os.environ[
        'alfred_workflow_data'] = '/Users/rhasija/Library/Application Support/Alfred 3/Workflow Data/org.javawithravi.alfred.workflow.stash'
    execute()
