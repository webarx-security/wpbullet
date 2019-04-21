from core.modules import BaseClass


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
