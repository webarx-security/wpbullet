from core.modules import BaseClass


# Class must have same name as filename
class CommandExecution(BaseClass):

    # Vulnerability name
    name = "Remote Command Execution"

    # Severity
    severity = "High"

    # Functions indicating vulnerability
    functions = [
        "eval",
        "popen",
        "system",
        "passthru",
        "exec",
        "shell_exec",
        "assert",
        "proc_open"
    ]

    # Functions that escape/filter user input
    #
    # Unless --no-blacklist flag is used, vulnerability
    # is ignored if one bellow matches before variable
    blacklist = [
        "escapeshellcmd"
    ]
