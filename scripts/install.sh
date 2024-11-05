# scripts/install.sh

#!/bin/bash

set -e

echo "Installing easysh..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install the package
pip install --editable .

echo "Installation complete. You can now use 'easysh' command."
