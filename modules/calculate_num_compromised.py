import dpkt
import socket

def calculate_num_compromised(pcap_file):
    """
    Calculates the 'num_compromised' attribute from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.

    Returns:
        int: The count of compromised systems.
    """
    num_compromised = 0
    for timestamp, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet is a TCP packet and has the payload
            if isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                payload = tcp.data.decode('utf-8', errors='ignore')

                # Check for compromise messages in the payload
                if 'compromised' in payload.lower():
                    num_compromised += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return num_compromised
