# easysh

`easysh` is a command-line tool that translates natural language commands into actual shell commands using the OpenAI ChatGPT API.

## Features

- Translate natural language instructions into shell commands.
- Securely store your OpenAI API key.
- Easy installation on Linux and macOS.

## Installation

### Prerequisites

- **Python 3.6+**
- **pip**

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/easysh.git
    cd easysh
    ```

2. **Run the Installation Script**

    ```bash
    ./scripts/install.sh
    ```

3. **Set the API Key**

    ```bash
    easysh --set-key
    ```

    Follow the prompt to enter your OpenAI API key.

## Usage

- **Translate a Natural Language Command**

    ```bash
    easysh open folder called abc
    ```

    **Output:**

    ```bash
    cd abc
    ```

- **Set or Update the OpenAI API Key**

    ```bash
    easysh --set-key
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
