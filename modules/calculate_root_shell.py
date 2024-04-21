import dpkt
import socket

def calculate_root_shell(pcap_file):
    """
    Calculates the 'root_shell' attribute from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.

    Returns:
        int: The count of root shell instances.
    """
    root_shell = 0
    for timestamp, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet is a TCP packet and has the payload
            if isinstance(tcp, dpkt.tcp.TCP) and len(tcp.data) > 0:
                payload = tcp.data.decode('utf-8', errors='ignore')

                # Check for root shell messages in the payload
                if 'root shell' in payload.lower():
                    root_shell += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return root_shell
