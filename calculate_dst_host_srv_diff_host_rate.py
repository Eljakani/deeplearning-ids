import dpkt
import socket
import collections


def calculate_dst_host_srv_diff_host_rate(pcap_file):
    """
    Calculates the dst_host_srv_diff_host_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The dst_host_srv_diff_host_rate value.
    """
    # Initialize a dictionary to keep track of the services and their associated destination hosts
    srv_dst_hosts = collections.defaultdict(lambda: collections.defaultdict(set))

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

            # Add the destination host to the set of hosts for the service
            srv_dst_hosts[service][dst_ip].add(timestamp)
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the dst_host_srv_diff_host_rate
    total_connections = sum(len(hosts) for hosts_per_srv in srv_dst_hosts.values() for hosts in hosts_per_srv.values())
    unique_host_counts = [len(set(hosts)) for hosts_per_srv in srv_dst_hosts.values() for hosts in
                          hosts_per_srv.values()]
    sum_unique_host_counts = sum(unique_host_counts)
    dst_host_srv_diff_host_rate = sum_unique_host_counts / total_connections if total_connections > 0 else 0

    return dst_host_srv_diff_host_rate
