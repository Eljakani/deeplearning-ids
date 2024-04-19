import dpkt
import socket


def calculate_dst_host_count(pcap_file):
    """
    Calculates the dst_host_count attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        int: The dst_host_count value.
    """
    # Initialize a set to keep track of the unique destination hosts
    dst_hosts = set()

    # Open the pcap file and process each packet
    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data

            # Get the destination IP address
            dst_ip = socket.inet_ntoa(ip.dst)

            # Add the destination IP to the set of destination hosts
            dst_hosts.add(dst_ip)
        except:
            # Skip any packets that can't be parsed
            continue   

    # Calculate the dst_host_count
    dst_host_count = len(dst_hosts)

    return dst_host_count
