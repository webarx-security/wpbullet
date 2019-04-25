from Modules import *
import os
from core import passive_check
from core.passive_check import passive_check as passive_check_processor
import requests
import re
import zipfile
import io
from terminaltables import AsciiTable, DoubleTable, SingleTable
from colorama import Fore, Back, Style
import shutil


CODE_VULNERABILITIES = [
    ['Severity', 'Vulnerability', 'File', 'Info']
]


# Main function to handle files processing
def scan(args):

    # Delete .temp folder from previous scan
    try:
        shutil.rmtree('.temp')
    except FileNotFoundError:
        pass

    # Plugin repository URL
    if args.path[:7] in ['https:/', 'http://'] and args.path[-4:] != ".zip":
        print(Fore.RED + '[ * ]' + Fore.RESET + " Downloading plugin from: " + args.path)
        download_url = scrape_plugin_download_url(args.path)
        download_plugin(download_url)
        args.path = ".temp/"

    # Plugin ZIP download URL
    if args.path[:7] in ['https:/', 'http://'] and args.path[-4:] == ".zip":
        print(Fore.RED + '[ * ]' + Fore.RESET + " Downloading ZIP plugin from: " + args.path)
        download_plugin(args.path)
        args.path = ".temp/"

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

    # Print registered admin actions
    table_instance = SingleTable(passive_check.ADMIN_ACTIONS_DATA, Fore.GREEN + " Admin Actions " + Style.RESET_ALL)
    table_instance.justify_columns[2] = 'left'
    print(table_instance.table)
    print()

    # Print registered ajax hooks
    table_instance = SingleTable(passive_check.AJAX_HOOKS_DATA, Fore.YELLOW + " Registered Hooks " + Style.RESET_ALL)
    table_instance.justify_columns[2] = 'left'
    print(table_instance.table)
    print()

    # Print vulnerabilities
    table_instance = SingleTable(CODE_VULNERABILITIES, Fore.YELLOW + " Found Vulnerabilities " + Style.RESET_ALL)
    table_instance.justify_columns[2] = 'left'
    print(table_instance.table)
    print()

    # Cleanup
    if args.cleanup:
        print("Doing cleanup")
        shutil.rmtree('.temp')


# Check given file for vulnerabilities
def check_file(file,r, modules):
    path = os.path.join(r, file)
    content = read_file(path)

    # Run passive check for user inputs
    passive_check_processor(content, path)

    # Run source code analysis
    process_file(content, path, modules)


# Process single given file, run all enabled modules
def process_file(content, file, modules):
    for module in classes:
        if modules['enabled'][0] != '':
            if module in modules['enabled']:
                classes[module].execute(classes[module], content, file)
        elif module not in modules['disabled']:
            classes[module].execute(classes[module], content, file)


# Read file and return It's content
def read_file(path):
    f = open(path, mode="r", encoding="latin1")
    if f.mode == 'r':
       contents = f.read()
       return contents


# Returns download URL from WordPress plugin repository page
def scrape_plugin_download_url(plugin_url):
    r = requests.get(plugin_url)
    response = r.text
    download_url = re.search('\"downloadUrl\": \"(.+)\",', response)[1].replace("\\", "")
    return download_url


# Downloads plugin from given URL and extracts it into .temp/
def download_plugin(download_url):
    r = requests.get(download_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(".temp")
