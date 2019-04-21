import Modules
import os


# Main function to handle files processing
def scan(args):

    files = scope_files(args.path)

    modules = {
        'enabled': [x.strip() for x in args.enabled.split(',')],
        'disabled': [x.strip() for x in args.disabled.split(',')]
    }

    file_no = 0
    for file in files:
        file_no = file_no + 1
        print(str(file_no) + "/" + str(len(files)), end="\r")
        content = read_file(file)
        process_file(content, file, modules)


# Process single given file, run all enabled modules
def process_file(content, file, modules):
    for module in dir(Modules):
        if '__' not in module:
            if modules['enabled'][0] != '':
                if module in modules['enabled']:
                    eval("Modules." + module + ".execute(Modules." + module + ", content, file)")
            elif module not in modules['disabled']:
                eval("Modules." + module + ".execute(Modules." + module + ", content, file)")


# Scope all .php files in the given path
def scope_files(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.php' in file:
                files.append(os.path.join(r, file))

    return files


# Read file and return It's content
def read_file(path):
    f = open(path, mode="r", encoding="latin1")
    if f.mode == 'r':
       contents = f.read()
       return contents
