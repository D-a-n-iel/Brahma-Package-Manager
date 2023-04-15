# Brahma-Package-Manager
A declarative package manager for Linux 

## How it works
Uses JSON configuration files that can define:
- A package
- A service
- A system installation

## Config file schema
```json
{
"package": {
        "name": "",
        "version": "",
        "definition": {
            "source": {
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
