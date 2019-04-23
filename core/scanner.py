from Modules import *
import os


# Main function to handle files processing
def scan(args):
    modules = {
        'enabled': [x.strip() for x in args.enabled.split(',')],
        'disabled': [x.strip() for x in args.disabled.split(',')]
    }

    count_files = 0
    for r, d, f in os.walk(args.path):
        for file in f:
            if '.php' in file:
                count_files = count_files + 1
                print('Checked files: ' + str(count_files), end="\r")
                check_file(file, r, modules)


def check_file(file,r, modules):
    path = os.path.join(r, file)
    content = read_file(path)
    process_file(content, path, modules)


# Process single given file, run all enabled modules
def process_file(content, file, modules):
    classes = {
        'CommandExecution': CommandExecution,
        'CrossSiteScripting': CrossSiteScripting,
        'FileInclusion': FileInclusion,
        'HeaderInjection': HeaderInjection,
        'InsecureEmail': InsecureEmail,
        'LDAPInjection': LDAPInjection,
        'OptionsUpdate': OptionsUpdate,
        'SQLInjection': SQLInjection,
        'XPATHInjection': XPATHInjection
    }
    for module in classes:
        if modules['enabled'][0] != '':
            if module in modules['enabled']:
                classes[module](content, file)
        elif module not in modules['disabled']:
            classes[module](content, file)


# Read file and return It's content
def read_file(path):
    f = open(path, mode="r", encoding="latin1")
    if f.mode == 'r':
       contents = f.read()
       return contents
