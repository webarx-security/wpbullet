from core.modules import BaseClass


class ArbitraryFileUpload(BaseClass):

    name = "Arbitrary File Upload"

    severity = "High"

    functions = [
        "move_uploaded_file"
    ]

    blacklist = []
