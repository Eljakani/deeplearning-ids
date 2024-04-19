import dpkt
import socket


def calculate_rerror_rate(pcap_file):
    """
    Calculates the rerror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The rerror_rate value.
    """
    # Initialize the number of rejected connections and the total number of connections
    rejected_conns = 0
    total_conns = 0

    # Open the pcap file and process each packet

    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Check if the packet has the RST flag set (rejected connection)
            if tcp.flags & dpkt.tcp.TH_RST:
                rejected_conns += 1

            # Increment the total number of connections
            total_conns += 1
        except:
            # Skip any packets that can't be parsed
            continue

    # Calculate the rerror_rate
    rerror_rate = rejected_conns / total_conns if total_conns > 0 else 0

    return rerror_rate