#!/bin/bash

set -e

echo "Installing easysh..."

# Upgrade pip
pip install --upgrade pip

# Install the package with the latest OpenAI library
pip install --upgrade openai
pip install --editable .

echo "Installation complete."

# Determine the appropriate local bin directory
if [ -d "$HOME/.local/bin" ]; then
    LOCAL_BIN="$HOME/.local/bin"
elif [ -d "$HOME/bin" ]; then
    LOCAL_BIN="$HOME/bin"
else
    mkdir -p "$HOME/.local/bin"
    LOCAL_BIN="$HOME/.local/bin"
fi

# Check if local bin is in PATH
if [[ ":$PATH:" != *":$LOCAL_BIN:"* ]]; then
    echo "Adding $LOCAL_BIN to PATH in ~/.zshrc"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
    echo "Please reload your shell or run 'source ~/.zshrc' to apply the changes."
else
    echo "$LOCAL_BIN is already in your PATH."
fi

echo "You can now use the 'easysh' command."
