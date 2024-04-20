from scapy.all import *
from scapy.layers.inet import TCP, IP


def calculate_is_host_login(packet):
    # Initialize host login flag
    is_host_login = 0

    # Define admin network subnet (e.g., '192.168.0.0/24')
    admin_subnet = '192.168.0.0/24'

    # Check if TCP layer exists
    if packet.haslayer(TCP):
        # Check protocol and ports (SSH, Telnet)
        if (packet[TCP].dport == 22 or packet[TCP].dport == 23) and (IP(packet).src.startswith(admin_subnet)):  #or IP(packet).dst.startswith(admin_subnet)
            is_host_login = 1

    return is_host_login