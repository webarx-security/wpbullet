from core.modules import BaseClass


class LDAPInjection(BaseClass):

    name = "LDAP Injection"

    severity = "High"

    functions = [
        "ldap_search",

    ]

    blacklist = []
