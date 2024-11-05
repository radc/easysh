# easysh/main.py

import sys
import os
import openai
import argparse
import configparser
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

def get_api_key():
    """Retrieve the OpenAI API key from the environment variable or config file, or prompt the user."""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    api_key = load_api_key()
    if api_key:
        return api_key

    # Prompt the user to enter the API key
    api_key = prompt_api_key()
    return api_key

def generate_command(prompt, api_key):
    """Generate the shell command using OpenAI's API."""
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use gpt-3.5-turbo if preferred
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates natural language instructions into shell commands."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0
        )
        command = response.choices[0].message['content'].strip()
        return command
    except openai.error.AuthenticationError:
        print("Error: Authentication failed. Please check your OpenAI API key.")
        sys.exit(1)
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Translate natural language into shell commands using OpenAI API.")
    parser.add_argument('message', nargs='*', help='Natural language command to translate.')
    parser.add_argument('--set-key', action='store_true', help='Set or update the OpenAI API key.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.set_key:
        api_key = prompt_api_key()
        print("API key has been set successfully.")
        sys.exit(0)

    if not args.message:
        print("Usage: easysh <natural language command>")
        print("       easysh --set-key  # To set or update the OpenAI API key")
        sys.exit(1)
    
    # Combine all arguments into a single prompt
    prompt = ' '.join(args.message)
    api_key = get_api_key()
    command = generate_command(prompt, api_key)
    print(command)
