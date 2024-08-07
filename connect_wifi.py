import argparse
import getpass

from utils import run_command


def connect_wifi(ssid, password):
    """Connect to a Wi-Fi network using nmcli."""
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
        connect_command = f"nmcli dev wifi connect {ssid} password {password}"

    result = run_command(connect_command)
    if result:
        print("Success")
    else:
        print("Failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect to a Wi-Fi network')
    parser.add_argument(
        'ssid', type=str,
        default="NguyenFamily",
        help='SSID of Wi-Fi network'
    )

    args = parser.parse_args()

    password = getpass.getpass(prompt='Enter Wi-Fi password: ')

    connect_wifi(args.ssid, password)
