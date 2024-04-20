from scapy.all import *
from scapy.layers.inet import TCP, IP


def calculate_num_shells(pcap_file):
    num_shells = 0

    for pkt in pcap_file:
        # Check if the packet is TCP
        if pkt.haslayer(TCP):
            # Get the source and destination IP addresses
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst

            # Check if the packet is outbound
            if src_ip != dst_ip:
                # Check if the packet contains a shell command
                if pkt[TCP].dport in [22, 23]:
                    num_shells += 1

    return num_shells
