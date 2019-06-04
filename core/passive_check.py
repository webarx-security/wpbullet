import re
from colorama import Fore
import copy

ADMIN_ACTIONS_DATA = [
    ['Action Name', 'Function', 'File'],
]

AJAX_HOOKS_DATA = [
    ['Action Name', 'Function', 'File', 'User Input'],
]

ADMIN_INIT_DATA = [
    ['Function', 'File', 'User Input']
]


def passive_check(content, path):
    scope_admin_actions(content, path)
    scope_ajax_hooks(content, path)
    scope_admin_init(content, path)


def scope_functions(content):
    functions = []
    pattern = r"function(\s+?)([a-zA-Z_0-9-]+?)(\s?)+\((.+)?\)(\s{0,}\S{0,}){"
    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        functions.append(match[1])
    return functions


def scope_ajax_hooks(content, file):
    pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(wp_ajax_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"

    # Functions with user input
    functions = scope_functions(content)

    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        user_inputs = function_has_user_input(content, functions, match[10])
        AJAX_HOOKS_DATA.append([match[4], match[10], file, (Fore.RED + ', ' + Fore.RESET).join(user_inputs)])


def scope_admin_actions(content, file):
    pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(admin_action_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        ADMIN_ACTIONS_DATA.append([match[4], match[10], file])


def scope_function_content(content, functions):
    results = {}
    for index, function in enumerate(functions):
        try:
            match = re.search(r'function(\s+)' + re.escape(function)+r'(\s|\S)+' + re.escape(functions[index + 1]), content)

        except IndexError:
            match = re.search(r'function(\s+)' + re.escape(function) + r'(\s|\S)+', content)
        results[function] = match.group(0)
    return results


def function_has_user_input(content, functions, function):
    functions_and_content = scope_function_content(content, functions)
    results = []
    if function in functions_and_content:
        matches = re.findall(r"((\$_GET|\$_POST|\$_REQUEST|\$_FILES|\$_COOKIE|\$_SESSION)(\s{0,}\[\s{0,}('|\\\")[a-zA-Z-_0-9]+('|\")\s{0,}\])|\$_SERVER(\s?)\[(\s?)+('|\\\"|`)(REQUEST_URI|PHP_SELF|HTTP_REFERER)(\s?)+('|\\\"|`)(\s?)+])", functions_and_content[function])
        for match in matches:
            results.append(match[0])
    return results


def scope_admin_init(content, file):
    content = copy.deepcopy(content)
    pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')\s{0,}admin_init\s{0,})(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=pattern, string=content)
    functions = []
    for match in matches:
        functions.append(match[9])

    all_functions = scope_functions(content)

    for function in functions:
        result = function_has_user_input(content, all_functions, function)
        if result:
            ADMIN_INIT_DATA.append([function, file, ', '.join(result)])
