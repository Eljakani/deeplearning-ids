from scapy.all import *
from io import BytesIO

def calculate_wrong_fragment(pcap_file_content):
    wrong_fragment_count = 0
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    for packet in packets:
        if packet.haslayer(IP) and packet.getlayer(IP).flags & 3 != 0:
            wrong_fragment_count += 1
    return wrong_fragment_count