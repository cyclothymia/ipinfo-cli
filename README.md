![](https://img.shields.io/github/issues/cyclothymia/ipinfo-cli)
![](https://img.shields.io/github/stars/cyclothymia/ipinfo-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# ipinfo-cli

A Command Line Interface (CLI) tool for retrieving information about IP addresses using the ipinfo.io API.

## Installation

To install `ipinfo-cli`, ensure you have Python and `pip` installed on your system. Then, run the following command:

```bash
pip install ipinfo-cli
```

## Usage

After installation, you can use `ipinfo-cli` to get information about a given IP address by running:

```bash
ipinfo-cli --ip <IP_ADDRESS>
```

A ipinfo.io token can be saved for further API information and negating rate limiting. This can be done by running:

```bash
ipinfo-cli --token <TOKEN>

# deleting the saved token
ipinfo-cli --delete-token
```

Saving the results to a JSON file can be done by running the following with the *EXACT* directory path and JSON file name:

```bash
ipinfo-cli --ip <IP_ADDRESS> --json <DIRECTORY>

# example
ipinfo-cli --ip <IP_ADDRESS> --json /path/to/file/output.json
```

| Argument | Description |
| --------- | ---------------- |
| --ip | Used to obtain information from a given IP address outputted in to readable data in the terminal. |
| --json | Saves the output to a JSON file in a given directory. |
| --token | Saves your ipinfo.io token to a file for future requests. |
| --delete-token | Deletes your ipinfo.io token to be replaced by another at another time. |

### Author

[cyclothymia](https://github.com/cyclothymia)

### License

Licenced under the MIT Licence
