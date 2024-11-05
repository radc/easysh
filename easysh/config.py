# easysh/config.py

import configparser
import os
import getpass

CONFIG_FILE = os.path.expanduser("~/.easysh_config")

def load_api_key():
    """Load the API key from the configuration file."""
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if 'OpenAI' in config and 'api_key' in config['OpenAI']:
            return config['OpenAI']['api_key']
    return None

def save_api_key(api_key):
    """Save the API key to the configuration file with restricted permissions."""
    config = configparser.ConfigParser()
    config['OpenAI'] = {'api_key': api_key}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    # Restrict file permissions to user only
    os.chmod(CONFIG_FILE, 0o600)

def prompt_api_key():
    """Prompt the user to enter their OpenAI API key."""
    print("Please enter your OpenAI API key. You can obtain it from https://platform.openai.com/account/api-keys")
    api_key = getpass.getpass("API Key: ")
    save_api_key(api_key)
    return api_key
