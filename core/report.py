import json
import random
import string
import re


def save_report(name, data, path):

    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    output = []
    if name == 'admin_actions':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'action_name': __(item[0]),
                'function': __(item[1]),
                'file': __(item[2])
            })

    elif name == 'ajax_hooks':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'action_name': __(item[0]),
                'function': __(item[1]),
                'file': __(item[2]),
                'user_input': __(item[3])
            })

    elif name == 'admin_init' or name == 'vulnerabilities':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'function': __(item[0]),
                'file': __(item[1]),
                'user_input': __(item[2])
            })

    with open('reports/' + path.split("/")[-1] + filename + '_' + name + '.json', 'w') as outfile:
        json.dump(output, outfile)


def __(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)