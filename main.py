from dpkt.pcap import Reader
from scapy.all import *
from scapy.layers.l2 import Ether
from modules import calculate_dst_bytes
from modules import calculate_flag


def dpkt_to_scapy(packet_data):
    """
    Convert a dpkt packet to a scapy packet.

    Args:
        packet_data (bytes): The raw packet data.

    Returns:
        scapy.packet.Packet: The scapy packet.
    """
    return Ether(packet_data)


pcap_file_path = 'C:\\Users\\HP\\Desktop\\Doss_Partage\\pcap.pcap'

with open(pcap_file_path, 'rb') as f:
    pcap = Reader(f)
    # Read one packet
    timestamp, packet_data = next(pcap)
    scapy_packet = dpkt_to_scapy(packet_data)

    flag = calculate_flag.calculate_flag(scapy_packet)

print(flag)
