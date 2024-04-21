import dpkt
import socket

def calculate_logged_in(pcap_file):
    """
    Calculates the 'logged_in' attribute from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.

    Returns:
        int: The count of successful login attempts.
    """
    logged_in = 0
    for timestamp, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet is a TCP packet and has the payload
            if isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                payload = tcp.data.decode('utf-8', errors='ignore')

                # Check for successful login messages in the payload
                if 'logged in' in payload.lower():
                    logged_in += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return logged_in