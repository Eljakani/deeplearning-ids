import dpkt
import collections


def calculate_srv_count(pcap_file):
    """
    Calculates the srv_count attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        int: The srv_count value.
    """
    # Initialize a set to keep track of the unique services
    services = set()

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

            # Add the service to the set of unique services
            services.add(service)
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the srv_count
    srv_count = len(services)

    return srv_count
