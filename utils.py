"""
utils.py

This module contains utility functions used across the application.

Functions:
    run_command(command: str) -> str:
        Run a shell command and return its output.
"""


import subprocess


def run_command(command):
    """
    Run a shell command and return its output.

    Args:
        command (str): Shell command to be executed.

    Returns:
        str: The standard output from the command if successful.
        None: If command fails, returns None and error message is printed.
    """
    try:
        result = subprocess.run(
            command, shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None
