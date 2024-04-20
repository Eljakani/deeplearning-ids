import dpkt
import socket
import collections


def calculate_dst_host_same_src_port_rate(pcap_file):
    """
    Calculates the dst_host_same_src_port_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The dst_host_same_src_port_rate value.
    """
    # Initialize a dictionary to keep track of the source ports and their associated destination hosts
    dst_host_src_ports = collections.defaultdict(lambda: collections.defaultdict(int))

    # Open the pcap file and process each packet
    pcap = pcap_file
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Get the destination IP address
            dst_ip = socket.inet_ntoa(ip.dst)

            # Get the source port
            src_port = tcp.sport

            # Increment the count for the source port and destination host
            dst_host_src_ports[dst_ip][src_port] += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the dst_host_same_src_port_rate
    total_connections = sum(sum(port_counts.values()) for port_counts in dst_host_src_ports.values())
    same_src_port_connections = sum(
        count ** 2 for port_counts in dst_host_src_ports.values() for count in port_counts.values())
    dst_host_same_src_port_rate = same_src_port_connections / (total_connections ** 2) if total_connections > 0 else 0

    return dst_host_same_src_port_rate
