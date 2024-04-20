import dpkt
import socket


def calculate_serror_rate(pcap_file):
    """
    Calculates the serror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The serror_rate value.
    """
    # Initialize the number of connection errors and the total number of connections
    conn_errors = 0
    total_conns = 0

    # Open the pcap file and process each packet
    pcap = pcap_file
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet has the RST or FIN flag set (connection error)
            if tcp.flags & (dpkt.tcp.TH_RST | dpkt.tcp.TH_FIN):
                conn_errors += 1

            # Increment the total number of connections
            total_conns += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the serror_rate
    serror_rate = conn_errors / total_conns if total_conns > 0 else 0

    return serror_rate
