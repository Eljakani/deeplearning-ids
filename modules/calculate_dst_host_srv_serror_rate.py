import dpkt
import socket
import collections


def calculate_dst_host_srv_serror_rate(pcap_file):
    """
    Calculates the dst_host_srv_serror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The dst_host_srv_serror_rate value.
    """
    # Initialize a dictionary to keep track of the services, destination hosts, and their associated connection stats
    srv_dst_host_stats = collections.defaultdict(
        lambda: collections.defaultdict(lambda: [0, 0]))  # [connections, errors]

    # Open the pcap file and process each packet
    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Get the source and destination ports (represents the service)
            src_port = tcp.sport
            dst_port = tcp.dport
            service = (src_port, dst_port)

            # Get the destination IP address
            dst_ip = socket.inet_ntoa(ip.dst)

            # Increment the connection count for the service and destination host
            srv_dst_host_stats[service][dst_ip][0] += 1

            # Check if the packet has the RST or FIN flag set (connection error)
            if tcp.flags & (dpkt.tcp.TH_RST | dpkt.tcp.TH_FIN):
                srv_dst_host_stats[service][dst_ip][1] += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the dst_host_srv_serror_rate
    total_conns = 0
    total_errors = 0
    for srv_stats in srv_dst_host_stats.values():
        for dst_host_stats in srv_stats.values():
            total_conns += dst_host_stats[0]
            total_errors += dst_host_stats[1]
    dst_host_srv_serror_rate = total_errors / total_conns if total_conns > 0 else 0

    return dst_host_srv_serror_rate
