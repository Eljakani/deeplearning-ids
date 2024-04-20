import dpkt
import collections


def calculate_diff_srv_rate(pcap_file):
    """
    Calculates the diff_srv_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The diff_srv_rate value.
    """
    # Initialize a set to keep track of the unique services
    unique_services = set()

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

            # Add the service to the set of unique services
            unique_services.add(service)
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the diff_srv_rate
    total_services = len(unique_services)
    total_conns = sum(1 for service in unique_services)
    diff_srv_rate = (total_services - 1) / total_conns

    return diff_srv_rate
