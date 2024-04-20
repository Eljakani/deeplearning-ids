import dpkt
import collections


def calculate_same_srv_rate(pcap_file):
    """
    Calculates the same_srv_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The same_srv_rate value.
    """
    # Initialize a dictionary to keep track of the number of connections for each service
    srv_conn_counts = collections.defaultdict(int)

    # Open the pcap file and process each packet

    pcap = pcap_file
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Get the source and destination ports (represents the service)
            src_port = tcp.sport
            dst_port = tcp.dport
            service = (src_port, dst_port)

            # Increment the connection count for the service
            srv_conn_counts[service] += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the same_srv_rate
    total_conns = sum(srv_conn_counts.values())
    squared_counts = [count ** 2 for count in srv_conn_counts.values()]
    sum_squared_counts = sum(squared_counts)
    same_srv_rate = sum_squared_counts / (total_conns ** 2) if total_conns > 0 else 0

    return same_srv_rate
