from core.modules import BaseClass
import copy


class OptionsUpdate(BaseClass):

    name = "WordPress Options Update"

    severity = "High"

    functions = [
        "update_option",
    ]

    blacklist = []

    def build_pattern(self, content, file):
        user_input = copy.deepcopy(self.user_input)

        variables = self.get_input_variables(self, content)

        if variables:
            user_input.extend(variables)

        pattern = r"((" + '|'.join(self.functions) + ")\s{0,}\(\s{0,}(" + '|'.join(user_input) + ").*)"

        return pattern
