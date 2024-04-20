from scapy.all import *

def calculate_land(packet):
    """
    Calculate the 'land' feature for a given packet.
    
    Args:
        packet (scapy.packet.Packet): The packet to analyze.
        
    Returns:
        int: 1 if the source and destination IP addresses and port numbers are the same, 0 otherwise.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)
        if ip_layer.src == ip_layer.dst and tcp_layer.sport == tcp_layer.dport:
            return 1
    return 0