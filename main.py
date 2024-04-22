import pyshark
import time

# Import custom functions from modules folder
from modules.calculate_protocol_type import calculate_protocol_type
from modules.calculate_service import calculate_service
from modules.calculate_flag import calculate_flag
from modules.calculate_src_bytes import calculate_src_bytes
from modules.calculate_dst_bytes import calculate_dst_bytes
from modules.calculate_land import calculate_land

proccessed_packets = []
max_packets_different_service = 10
packets_with_different_service_count = 0

def packet_callback(packet):
    global packets_with_different_service_count

    service = calculate_service(packet)
    if service != "other":
        packets_with_different_service_count += 1

    # Append a new packet to the list with a mapping
    proccessed_packets.append({
        'protocol_type': calculate_protocol_type(packet),
        'service': service,
        'flag': calculate_flag(packet),
        'src_bytes': calculate_src_bytes(packet),
        'dst_bytes': calculate_dst_bytes(packet),
        'land': calculate_land(packet),
    })
    print(proccessed_packets[-1])

    if packets_with_different_service_count >= max_packets_different_service:
        # Stop the sniffing process
        capture.close()
        print(f"Reached the maximum of {max_packets_different_service} packets with service different than 'other'. Sniffing stopped.")

# Sniff packets from all interfaces
capture = pyshark.LiveCapture(bpf_filter="tcp or udp or icmp", display_filter=None)
capture.apply_on_packets(packet_callback, timeout=100)

# Log the time of sniffing
sniff_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Store packets in a pcap file
pcap_file = "sniffed_packets.pcap"
capture.write_pcap(pcap_file, proccessed_packets)