# Janus Package Manager
A declarative package manager for Linux 

## How it works
Uses JSON configuration files that can define:
- A package
- A service

## Installation

To clone this repository and enter the source directory:
```shell
git clone https://github.com/D-a-n-iel/janus
cd janus
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
