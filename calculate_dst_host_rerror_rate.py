import dpkt
import socket
import collections


def calculate_dst_host_rerror_rate(pcap_file):
    """
    Calculates the dst_host_rerror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The dst_host_rerror_rate value.
    """
    # Initialize a dictionary to keep track of the connections and rejected connections for each destination host
    dst_host_stats = collections.defaultdict(lambda: [0, 0])  # [connections, rejected_connections]

    # Open the pcap file and process each packet
    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Get the destination IP address
            dst_ip = socket.inet_ntoa(ip.dst)

            # Increment the connection count for the destination host
            dst_host_stats[dst_ip][0] += 1

            # Check if the packet has the RST flag set (rejected connection)
            if tcp.flags & dpkt.tcp.TH_RST:
                dst_host_stats[dst_ip][1] += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the dst_host_rerror_rate
    total_conns = sum(stats[0] for stats in dst_host_stats.values())
    total_rejected = sum(stats[1] for stats in dst_host_stats.values())
    dst_host_rerror_rate = total_rejected / total_conns if total_conns > 0 else 0

    return dst_host_rerror_rate
