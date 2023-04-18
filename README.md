# Janus Package Manager
A declarative package manager for Linux 

## How it works
Uses JSON configuration files that can define:
- A package
- A service

## Installation
Janus depends on [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), and the [GNU tool chain](https://www.nongnu.org/avr-libc/user-manual/install_tools.html).
Most GNU/Linux systems are bundled with these. However, installation instructions for each can be found in the provided links.

To clone this repository and enter the source directory:
```shell
git clone https://github.com/D-a-n-iel/janus
cd janus
```

To install the python dependencies:
```shell
pip install -r requirements.txt
```

Janus can then install itself!
```shell
python3 janus.py examples/janus.json
```

## Config file schema
```json
{
"package": {
        "name": "",
        "version": "",
        "definition": {
            "source": {
                "required-files": [""],
                "http-download": { "url": "",  "hash": ""},
                "git-fetch": { "url": "", "branch": "" }
            },
            "patch": {
                "replace-matches": [{ "str1": "", "str2": ""}],
                "create-symlinks": [{ "src": "", "dst": "" }],
                "commands": [""]
            },
            "build": {
                "system": "",
                "commands": [""]
            },
            "install": {
                "system": "",
                "make-executable": [""],
                "file-copy": [{ "file": "", "destination": "" }],
                "commands": [""]
            }
            "service": {
                "start-commands": [[""]],
                "stop-commands": [[""]],
                "restart-commands": [[""]]
            }
        }
    }
}
```

## Running tests
``` sh
python tests/test.py
```
