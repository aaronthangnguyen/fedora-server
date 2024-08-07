# FEDORA SERVER

## Dynamic DNS

1. Get public IP address by running `curl api.ipify.org`
2. Add A record to DNS pointing to public IP address, with **Proxied** option disabled
3. Get MAC address by running `ifconfig`
4. Reserve DHCP lease for MAC address with fixed local IP
5. Forward local IP to port 22
