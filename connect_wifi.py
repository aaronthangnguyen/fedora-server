"""
connect_wifi.py

This script connects to Wi-Fi network using provided SSID and password.

Usage:
    python connect_wifi.py --ssid <SSID>

Arguments:
    SSID: SSID of the Wi-Fi network to connect to.

Example:
    python connect_wifi.py --ssid MyHomeNetwork
"""

import argparse
import getpass
from utils import run_command


def connect_wifi(ssid, wifi_password):
    """
    Connect to a Wi-Fi network using nmcli.

    Args:
        ssid (str): SSID of Wi-Fi network to connect to.
        wifi_password (str): Password for Wi-Fi network.

    Returns:
        None
    """
    print(f"Connecting to SSID: {ssid}")

    # Check if the SSID is already known
    check_command = f"nmcli connection show | grep {ssid}"
    result = run_command(check_command)

    if result:
        # SSID is known, bring up the connection
        print("SSID known, bringing up connection...")
        connect_command = f"nmcli connection up {ssid}"
    else:
        # SSID is not known, create a new connection
        print("SSID not known, creating new connection...")
        connect_command = f"nmcli dev wifi connect {
            ssid} password {wifi_password}"

    result = run_command(connect_command)
    if result:
        print("Success")
    else:
        print("Failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect to a Wi-Fi network')
    parser.add_argument(
        '--ssid', type=str,
        default="NguyenFamily",
        help='SSID of Wi-Fi network'
    )

    args = parser.parse_args()

    wifi_password = getpass.getpass(prompt='Enter Wi-Fi password: ')

    connect_wifi(args.ssid, wifi_password)
