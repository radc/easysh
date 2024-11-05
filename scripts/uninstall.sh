#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting the uninstallation of easysh..."

# Function to uninstall via pip
uninstall_pip() {
    if command -v pip &> /dev/null; then
        echo "Attempting to uninstall easysh using pip..."
        pip uninstall easysh -y
    else
        echo "pip is not installed or not found in PATH."
    fi
}

# Function to uninstall via pipx
uninstall_pipx() {
    if command -v pipx &> /dev/null; then
        if pipx list | grep -q "easysh"; then
            echo "Attempting to uninstall easysh using pipx..."
            pipx uninstall easysh
        else
            echo "easysh is not installed via pipx."
        fi
    else
        echo "pipx is not installed or not found in PATH."
    fi
}

# Function to remove configuration files
remove_config_files() {
    CONFIG_FILE="$HOME/.easysh_config"
    LOG_FILE="$HOME/.easysh.log"
    
    echo "Removing configuration files..."
    
    if [ -f "$CONFIG_FILE" ]; then
        rm "$CONFIG_FILE"
        echo "Removed $CONFIG_FILE"
    else
        echo "Configuration file $CONFIG_FILE does not exist."
    fi
    
    if [ -f "$LOG_FILE" ]; then
        rm "$LOG_FILE"
        echo "Removed $LOG_FILE"
    else
        echo "Log file $LOG_FILE does not exist."
    fi
}

# Function to remove PATH modifications from shell config
clean_shell_config() {
    SHELL_CONFIG=""
    
    # Detect which shell is being used
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.bash_profile"
    fi
    
    echo "Cleaning PATH modifications in $SHELL_CONFIG..."
    
    # Backup the original shell config
    cp "$SHELL_CONFIG" "${SHELL_CONFIG}.backup"
    
    # Remove the specific export line added during installation
    sed -i.bak '/export PATH="\$HOME\/\.local\/bin:\$PATH"/d' "$SHELL_CONFIG"
    
    echo "PATH modifications removed from $SHELL_CONFIG"
    echo "A backup of your shell config has been created at ${SHELL_CONFIG}.backup"
}

# Function to remove the virtual environment (Optional)
remove_virtualenv() {
    read -p "Do you want to remove the virtual environment directory (e.g., venv/)? [y/N]: " choice
    case "$choice" in 
      y|Y ) 
        if [ -d "../venv" ]; then
            rm -rf ../venv
            echo "Removed virtual environment directory ../venv"
        else
            echo "Virtual environment directory ../venv does not exist."
        fi
        ;;
      * ) 
        echo "Skipped removing virtual environment."
        ;;
    esac
}

# Execute the functions
uninstall_pip
uninstall_pipx
remove_config_files
clean_shell_config
remove_virtualenv

echo "Uninstallation of easysh completed successfully."
