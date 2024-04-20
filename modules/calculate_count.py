import dpkt


def calculate_count(pcap_file):
    """
    Calculates the count attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        int: The count value.
    """
    count = 0

    # Open the pcap file and process each packet

    pcap = dpkt.pcap.Reader(pcap_file)
    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data

            # Increment the count for each TCP connection
            if isinstance(tcp, dpkt.tcp.TCP):
                count += 1
        except:
            # Skip any packets that can't be parsed
            continue

    return count
