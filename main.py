from dpkt.pcap import Reader
from scapy.all import *
from scapy.layers.l2 import Ether
from modules import calculate_srv_diff_host_rate
from modules import calculate_dst_bytes
from modules import calculate_dst_host_count
from modules import calculate_count
from modules import calculate_diff_srv_rate


def dpkt_to_scapy(packet_data):
    """
    Convert a dpkt packet to a scapy packet.

    Args:
        packet_data (bytes): The raw packet data.

    Returns:
        scapy.packet.Packet: The scapy packet.
    """
    return Ether(packet_data)


pcap_file_path = 'C:\\Users\\el mahdi\\Desktop\\dataset AI\\test.pcap'

with open(pcap_file_path, 'rb') as f:
    pcap = Reader(f)
    # Read one packet
    timestamp, packet_data = next(pcap)
    scapy_packet = dpkt_to_scapy(packet_data)

    flag = calculate_count.calculate_count(pcap)
    #flag1 = calculate_diff_srv_rate.calculate_diff_srv_rate(pcap)
    flag3 = calculate_dst_bytes.calculate_dst_bytes(scapy_packet)
    flag4 = calculate_srv_diff_host_rate.calculate_srv_diff_host_rate(pcap)
    flag2 = calculate_dst_host_count.calculate_dst_host_count(pcap)


print(flag, flag2, flag3, flag4)
