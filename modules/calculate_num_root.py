import dpkt
import socket


def calculate_num_root(pcap_file):
    """
    Calculates the 'num_root' attribute from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.

    Returns:
        int: The count of root access instances.
    """
    num_root = 0
    for timestamp, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet is a TCP packet and has the payload
            if isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                payload = tcp.data.decode('utf-8', errors='ignore')

                # Check for root access messages in the payload
                if 'root access' in payload.lower():
                    num_root += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return num_root
