# Janus Package Manager
A declarative package manager for Linux 

## How it works
Janus uses JSON configuration files that can define a package or service, or both

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

## Usage
For these examples the `vim.json` and `nginx.json` files located under the `examples/` directory will be used.

### Package installation
A full path to the package file can be provided:
```shell
janus examples/vim.json
```

If the `vim.json` file was located under `$XDG_CONFIG_HOME/janus/` directory,
it could be referred to without the need for the file extension:
```shell
janus vim
```

### Services
The user must indicate when they want to use a service rather than the whole package,
and what to do with the service; be it *start*ing, *restart*ing, or *stop*ping it.

For example, if the example `nginx.json` package was installed, its web server could be Started with:
```shell
janus service start examples/nginx.json
```

The same file extension ellision rule applies if the package file is under `$XDG_CONFIG_HOME/janus/`:
```shell
janus service start nginx
```

Stopping and Restarting a service follow the same rule too:
```shell
janus service restart nginx
janus service stop nginx
```

These commands would in turn restart the currently running nginx web server, and then stop it.

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
                "prefix": "",
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
