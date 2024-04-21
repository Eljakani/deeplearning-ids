import dpkt
import socket

def calculate_num_file_creations(pcap_file):
    """
    Calculates the 'num_file_creations' attribute from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.

    Returns:
        int: The count of file creation instances.
    """
    num_file_creations = 0

    for timestamp, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet is a TCP packet and has the payload
            if isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                payload = tcp.data.decode('utf-8', errors='ignore')

                # Check for file creation messages in the payload
                if 'file created' in payload.lower():
                    num_file_creations += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return num_file_creations
