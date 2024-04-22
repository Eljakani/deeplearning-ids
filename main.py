import sniffer
from modules.calculate_protocol_type import calculate_protocol_type
from modules.calculate_service import calculate_service
from modules.calculate_flag import calculate_flag
from modules.calculate_src_bytes import calculate_src_bytes
from modules.calculate_dst_bytes import calculate_dst_bytes
from modules.calculate_land import calculate_land
from scapy.all import *

processed_packets = []

# Read the PCAP file
pcap_file = 'valid_packets.pcap'
packets = rdpcap(pcap_file)

# Iterate over the packets
for packet in packets:
    processed_packet = {
        'protocol_type': calculate_protocol_type(packet),
        'service': calculate_service(packet),
        'flag': calculate_flag(packet),
        'src_bytes': calculate_src_bytes(packet),
        'dst_bytes': calculate_dst_bytes(packet),
        'land': calculate_land(packet),
    }
    processed_packets.append(processed_packet)

print(processed_packets)