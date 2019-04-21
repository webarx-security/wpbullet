from core.modules import BaseClass


class InsecureEmail(BaseClass):

    name = "Insecure Email"

    severity = "High"

    functions = [
        "mail",
    ]

    blacklist = []
