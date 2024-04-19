import dpkt
import collections


def calculate_srv_rerror_rate(pcap_file):
    """
    Calculates the srv_rerror_rate attribute from a pcap file.

    Args:
        pcap_file (str): Path to the pcap file.

    Returns:
        float: The srv_rerror_rate value.
    """
    # Initialize a dictionary to keep track of the number of connections and rejected connections for each service
    srv_stats = collections.defaultdict(lambda: [0, 0])  # [connections, rejected_connections]

    # Open the pcap file and process each packet
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
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

                # Check if the packet has the RST flag set (rejected connection)
                if tcp.flags & dpkt.tcp.TH_RST:
                    srv_stats[service][1] += 1
            except:
                # Skip any packets that can't be parsed
                continue

    # Calculate the srv_rerror_rate
    total_conns = sum(stats[0] for stats in srv_stats.values())
    total_rejected = sum(stats[1] for stats in srv_stats.values())
    srv_rerror_rate = total_rejected / total_conns if total_conns > 0 else 0

    return srv_rerror_rate


# Example usage
pcap_file = 'C:\\Users\\HP\\Desktop\\Doss_Partage\\pcapp.pcap'
srv_rerror_rate = calculate_srv_rerror_rate(pcap_file)
print(f"srv_rerror_rate: {srv_rerror_rate}")