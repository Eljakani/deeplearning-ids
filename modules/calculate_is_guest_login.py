from scapy.all import *
from scapy.layers.inet import TCP, IP


def calculate_is_guest_login(packet):
    # Initialize guest login flag
    is_guest_login = 0

    # Define guest network subnet (e.g., '192.168.1.0/24')
    guest_subnet = '192.168.1.0/24'

    # Check if TCP layer exists
    if packet.haslayer(TCP):
        # Check protocol and ports (FTP, HTTP, HTTPS)
        if (packet[TCP].dport == 21 or packet[TCP].dport == 80 or packet[TCP].dport == 443) \
            and (IP(packet).src.startswith(guest_subnet) or IP(packet).dst.startswith(guest_subnet)):
            is_guest_login = 1

    return is_guest_login
