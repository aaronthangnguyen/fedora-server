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


def private_ip():
    """
    Get private IP address of machine.

    Returns:
        str: Private IP address.
        None: If there is an error obtaining private IP address.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Use Google's public DNS server
            private_ip = s.getsockname()[0]
        return private_ip
    except Exception as e:
        print(f"Error obtaining private IP address: {e}")
        return None


def public_ip():
    """
    Get public IP address of machine by querying api.ipify.org.

    Returns:
        str: Public IP address.
        None: If there is an error obtaining public IP address.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        print(f"Error obtaining public IP address: {e}")
        return None


if __name__ == "__main__":
    print(f"Private IP: {private_ip()}")
    print(f"Public IP: {public_ip()}")
