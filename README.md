# Project Setup and Execution Guide

This guide provides instructions on how to set up a Python virtual environment and run the `Projeto.py` script using the Windows Subsystem for Linux (WSL).

## Prerequisites

1. **Windows Subsystem for Linux (WSL)**: Make sure WSL is installed on your Windows machine. You can follow the official [WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install) if you haven't installed it yet.
2. **Python**: Ensure that Python is installed in your WSL environment. You can verify this by running:

    ```bash
    python3 --version
    ```

   If Python is not installed, you can install it by running:

    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

3. **Git**: Make sure Git is installed to clone the repository:

    ```bash
    sudo apt install git
    ```

## Instructions

To set up the virtual environment and run the `Projeto.py` script, execute the following commands:

```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Run the script
python Projeto.py

# Deactivate the virtual environment after running the script
deactivate
