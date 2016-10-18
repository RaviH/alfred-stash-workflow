import os
import re
from alfred_config import read_config


def find_acct(entry, word):
    found = word in entry
    return found


def get_username():
    username = get_username_from_key_chain()

    if username is None:
        username = get_username_from_config()

    if username is None:
        username = "Please setup configuration correctly: username info missing."

    return username


def get_username_from_config():
    return read_config('username')


def get_username_from_key_chain():
    output = os.popen("security find-internet-password -j \"org.javawithravi.stash.workflow11\" -g").read()
    output_list = output.split("\n")
    account_strings = [x for x in output_list if find_acct(x, 'acct')]
    if account_strings:
        account_string = account_strings[0]
        m = re.search('.*\"(\w*)\"', account_string)
        return m.group(1)
    else:
        return None


def get_password():
    output = os.popen("security 2>&1 >/dev/null find-internet-password -j \"org.javawithravi.stash.workflow1\" -g").read()
    matches = re.search('.*: \"(.*)\".*', output)
    if matches:
        return matches.group(1)
    else:
        return  read_config('password', True)


if __name__ == '__main__':
    print get_username()
    print get_password()
