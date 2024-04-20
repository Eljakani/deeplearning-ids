from scapy.all import *
from io import BytesIO

def calculate_urgent(pcap_file_content):
    urgent_count = 0
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    for packet in packets:
        if packet.haslayer(TCP) and packet.getlayer(TCP).flags & 0x20:
            urgent_count += 1
    return urgent_count