from core.modules import BaseClass
import copy

class CrossSiteScripting(BaseClass):

    name = "Cross site scripting"

    severity = "Medium"

    functions = [
        "print",
        "echo",
        "printf"
    ]

    blacklist = [
        "htmlspecialchars",
        "esc_html",
        "sanitize_text_field",
        "\(?(\s?)+int(\s?)+\)",
        "htmlentities",
        "esc_attr"
    ]

    # Build dynamic regex pattern to locate vulnerabilities in given content
    def build_pattern(self, content, file):
        user_input = copy.deepcopy(self.user_input)
        functions = copy.deepcopy(self.functions)

        variables = self.get_input_variables(self, content)

        if variables:
            user_input.extend(variables)

        if self.blacklist:
            blacklist_pattern = r"(?!(\s?)+(.*(" + '|'.join(self.blacklist) + ")))"
        else:
            blacklist_pattern = ""

        functions = [self.functions_prefix + x for x in functions]

        pattern = r"((" + '|'.join(functions) + ")\s{0,}\(?\s{0,1}" + blacklist_pattern + ".*(" + '|'.join(user_input) + ").*)"
        return pattern
