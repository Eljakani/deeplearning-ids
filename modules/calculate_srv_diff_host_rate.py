import dpkt
import collections


def calculate_srv_diff_host_rate(pcap_file):
    """
    Calculates the srv_diff_host_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The srv_diff_host_rate value.
    """
    # Initialize a dictionary to keep track of the services and their associated hosts
    srv_hosts = collections.defaultdict(set)

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

            # Get the source and destination IP addresses (represents the hosts)
            src_ip = ip.src
            dst_ip = ip.dst

            # Add the source and destination hosts to the set of hosts for the service
            srv_hosts[service].add(src_ip)
            srv_hosts[service].add(dst_ip)
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the srv_diff_host_rate
    total_conns = sum(len(hosts) for hosts in srv_hosts.values())
    unique_host_counts = [len(set(hosts)) for hosts in srv_hosts.values()]
    sum_unique_host_counts = sum(unique_host_counts)
    srv_diff_host_rate = sum_unique_host_counts / total_conns if total_conns > 0 else 0

    return srv_diff_host_rate
