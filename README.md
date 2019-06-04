![alt text](https://raw.githubusercontent.com/webarx-security/wpbullet/dev/screenshots/1.png "Logo Title Text 1")



# wpBullet [![Build Status](https://travis-ci.org/webarx-security/wpbullet.svg?branch=dev)](https://travis-ci.org/webarx-security/wpbullet) [![Python 2.x|3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://github.com/webarx-security/wpbullet/blob/dev/LICENSE)
A static code analysis for WordPress Plugins/Themes (and PHP)


## Installation
Simply clone the repository, install requirements and run the script 
- `$ git clone https://github.com/webarx-security/wpbullet wpbullet` 
- `$ cd wpbullet`
- `$ pip install -r requirements.txt`
- `$ python wpbullet.py`


## Usage
Available options:
```
--path (required) System path or download URL 
Examples:
--path="/path/to/plugin"
--path="https://wordpress.org/plugins/example-plugin"
--path="https://downloads.wordpress.org/plugin/example-plugin.1.5.zip"

--enabled (optional) Check only for given modules, ex. --enabled="SQLInjection,CrossSiteScripting"
--disabled (optional) Don't check for given modules, ex. --disabled="SQLInjection,CrossSiteScripting"
--cleanup (optional) Automatically remove content of .temp folder after scanning remotely downloaded plugin (boolean)
--report (optional) Saves result inside reports/ directory in JSON format (boolean)

$ python wpbullet.py --path="/var/www/wp-content/plugins/plugin-name"
```

## Creating modules
Creating a module is flexible and allows for override of the `BaseClass` methods for each module as well as creating their own methods

Each module in `Modules` directory is implementing properties and methods from `core.modules.BaseClass`,
thus each module's required parameter is `BaseClass`

Once created, module needs to be imported in `modules/__init__.py`. Module and class name must be consistent
in order to module to be loaded.

__If you are opening pull request to add new module, please provide unit tests for your module as well.__


### Module template

`Modules/ExampleVulnerability.py`
```python
from core.modules import BaseClass


class ExampleVulnerability(object):

    # Vulnerability name
    name = "Cross-site Scripting"

    # Vulnerability severity
    severity = "Low-Medium"

    # Functions causing vulnerability
    functions = [
        "print"
        "echo"
    ]

    # Functions/regex that prevent exploitation
    blacklist = [
        "htmlspecialchars",
        "esc_attr"
    ]

```

#### Overriding regex match pattern
Regex pattern is being generated in `core.modules.BaseClass.build_pattern` and therefore can be overwritten in 
each module class.

`Modules/ExampleVulnerability.py`
```python
import copy


...
# Build dynamic regex pattern to locate vulnerabilities in given content
def build_pattern(self, content, file):
    user_input = copy.deepcopy(self.user_input)

    variables = self.get_input_variables(self, content)

    if variables:
        user_input.extend(variables)

    if self.blacklist:
        blacklist_pattern = r"(?!(\s?)+(.*(" + '|'.join(self.blacklist) + ")))"
    else:
        blacklist_pattern = ""

    self.functions = [self.functions_prefix + x for x in self.functions]

    pattern = r"((" + '|'.join(self.functions) + ")\s{0,}\(?\s{0,1}" + blacklist_pattern + ".*(" + '|'.join(user_input) + ").*)"
    return pattern
```

### Testing
Running unit tests: `$ python3 -m unittest`
