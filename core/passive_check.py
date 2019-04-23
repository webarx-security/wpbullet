import re
from terminaltables import AsciiTable, DoubleTable, SingleTable
from colorama import Fore, Back, Style
import copy


ADMIN_ACTIONS_DATA = [
    ['Action Name', 'Function', 'File'],
]

AJAX_HOOKS_DATA = [
    ['Action Name', 'Function', 'File'],
]


def passive_check(content, path):
    scope_admin_actions(content, path)
    scope_ajax_hooks(content, path)


def scope_functions(content):
    pattern = r"function(\s+?)([a-zA-Z_0-9-]+?)(\s?)+\((.+?)\)(\s{0,}\S{0,}){"
    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        print(match[1])


def scope_ajax_hooks(content, file):
    pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(wp_ajax_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        AJAX_HOOKS_DATA.append([match[4], match[10], file])


def scope_admin_actions(content, file):
    pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(admin_action_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=pattern, string=content)
    for match in matches:
        ADMIN_ACTIONS_DATA.append([match[4], match[10], file])
