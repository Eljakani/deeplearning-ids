import dpkt
import socket
import collections


def calculate_dst_host_count(pcap_file):
    """
    Calculates the Dst_host_count attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The Dst_host_count value.
    """
    # Initialize a dictionary to keep track of the destination hosts
    dst_hosts = collections.defaultdict(set)

    # Open the pcap file and process each packet

    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data

            # Get the destination IP address
            dst_ip = socket.inet_ntoa(ip.dst)

            # Add the destination IP to the set of destination hosts
            dst_hosts[dst_ip].add(timestamp)
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the Dst_host_count
    dst_host_count = sum(len(timestamps) for timestamps in dst_hosts.values())

    return dst_host_count


# Example usage
pcap_file = 'C:\\Users\\HP\\Desktop\\Doss_Partage\\pcap.pcap'
dst_host_count = calculate_dst_host_count(pcap_file)
print(f"Dst_host_count: {dst_host_count}")