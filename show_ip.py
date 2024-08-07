"""
show_ip.py

This script retrieves and displays private and public IP addresses.

Usage:
    python3 show_ip.py

Example:
    python3 show_ip.py
"""

import socket
import requests
from requests.exceptions import RequestException


def get_private_ip():
    """
    Get the private IP address of the machine.

    Returns:
        str: The private IP address.
        None: If there is an error obtaining the private IP address.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Use Google's public DNS server
            private_ip = s.getsockname()[0]
        return private_ip
    except OSError as e:
        print(f"Error obtaining private IP address: {e}")
        return None


def get_public_ip():
    """
    Get the public IP address of the machine by querying api.ipify.org.

    Returns:
        str: The public IP address.
        None: If there is an error obtaining the public IP address.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except RequestException as e:
        print(f"Error obtaining public IP address: {e}")
        return None


if __name__ == "__main__":
    private_ip_addr = get_private_ip()
    public_ip_addr = get_public_ip()

    if private_ip_addr:
        print(f"Private IP: {private_ip_addr}")
    else:
        print("Could not determine private IP address.")

    if public_ip_addr:
        print(f"Public IP: {public_ip_addr}")
    else:
        print("Could not determine public IP address.")
