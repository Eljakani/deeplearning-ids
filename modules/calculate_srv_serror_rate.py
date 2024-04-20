import dpkt
import collections


def calculate_srv_serror_rate(pcap_file):
    """
    Calculates the srv_serror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The srv_serror_rate value.
    """
    # Initialize a dictionary to keep track of the number of connections and errors for each service
    srv_stats = collections.defaultdict(lambda: [0, 0])  # [connections, errors]

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
            srv_stats[service][0] += 1

            # Check if the packet has the RST or FIN flag set (connection error)
            if tcp.flags & (dpkt.tcp.TH_RST | dpkt.tcp.TH_FIN):
                srv_stats[service][1] += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the srv_serror_rate
    total_conns = sum(stats[0] for stats in srv_stats.values())
    total_errors = sum(stats[1] for stats in srv_stats.values())
    srv_serror_rate = total_errors / total_conns if total_conns > 0 else 0

    return srv_serror_rate
