from core.modules import BaseClass


class HeaderInjection(BaseClass):

    name = "Header Injection"

    severity = "Medium"

    functions = [
        "header",
        "HttpMessage::setHeaders",
        "HttpRequest::setHeaders"
    ]

    blacklist = []
