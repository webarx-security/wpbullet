from core.modules import BaseClass


class XPATHInjection(BaseClass):

    name = "XPATH Injection"

    severity = "High"

    functions = [
        "xpath",

    ]

    blacklist = []
