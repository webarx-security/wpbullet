import Modules
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
    for module in dir(Modules):
        if '__' not in module:
            if modules['enabled'][0] != '':
                if module in modules['enabled']:
                    eval("Modules." + module + ".execute(Modules." + module + ", content, file)")
            elif module not in modules['disabled']:
                eval("Modules." + module + ".execute(Modules." + module + ", content, file)")


# Read file and return It's content
def read_file(path):
    f = open(path, mode="r", encoding="latin1")
    if f.mode == 'r':
       contents = f.read()
       return contents
