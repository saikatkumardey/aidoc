# aidoc

aidoc is a command line interface (CLI) tool that uses AI to automatically generate documentation for your code.

[![PyPI](https://badge.fury.io/py/aidoc.svg)](https://pypi.org/project/aidoc/0.1.1/)

## Requirements

- OpenAI API key: [https://beta.openai.com/](https://beta.openai.com/)
- Python 3.6 or higher


## Installation

- standalone

```
python3 -m pip install aidoc
```

- create a virtual environment and install the package (recommended)

```bash
pip install aidoc
```

## Usage

To configure the API key and model for aidoc, run the following command:

```
aidoc configure
```

To generate documentation for a source file or directory, run the following command:

```
aidoc gen <source_file>
```

You can also specify the following optional arguments:

- `-o` or `--overwrite`: Overwrite existing docstrings
- `-f` or `--format`: Format the entire source file using black (default=True)
- `-pr` or `--pull-request`: Create a pull request with the changes

## Examples

**Generate docstrings for the main.py file:**

```
aidoc gen main.py
```

**Generate docstrings for all Python files in the src directory and its subdirectories:**

```
aidoc gen src
```

**Generate docstrings and create a pull request with the changes:**

```
aidoc gen main.py -pr
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [OpenAI](https://openai.com/)

## Disclaimer

This project is not affiliated with OpenAI. The OpenAI API and GPT-3 language model are not free. You will need to sign up for a free [OpenAI](https://beta.openai.com/) account and create an API key to use this tool.