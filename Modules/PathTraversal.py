from core.modules import BaseClass


class PathTraversal(BaseClass):

    name = "Path Traversal"

    severity = "High"

    functions = [
        "file_get_contents",

    ]

    blacklist = [
        "basename",
        "realpath"
    ]
