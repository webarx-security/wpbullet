from core.modules import BaseClass


class FileInclusion(BaseClass):

    name = "File Inclusion"

    severity = "High"

    functions = [
        "virtual",
        "include",
        "require",
        "include_once",
        "require_once",
        "readfile",
        "show_source",
        "fopen",
        "file",
        "fpassthru",
        "gzopen",
        "gzfile",
        "gzpassthru",
        "readgzfile",
        "move_uploaded_file"
    ]

    blacklist = []
