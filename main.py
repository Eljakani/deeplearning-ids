from modules.calculate_protocol_type import calculate_protocol_type
from modules.calculate_service import calculate_service
from modules.calculate_flag import calculate_flag
from modules.calculate_src_bytes import calculate_src_bytes
from modules.calculate_dst_bytes import calculate_dst_bytes
from modules.calculate_land import calculate_land
from modules.calculate_wrong_fragment import calculate_wrong_fragment
from modules.calculate_urgent import calculate_urgent
from modules.calculate_hot import calculate_hot
from modules.calculate_num_failed_logins import calculate_num_failed_logins
from modules.calculate_logged_in import calculate_logged_in
from modules.calculate_num_compromised import calculate_num_compromised
from modules.calculate_root_shell import calculate_root_shell
from modules.calculate_su_attempted import calculate_su_attempted
from modules.calculate_num_root import calculate_num_root
from modules.calculate_num_file_creations import calculate_num_file_creations
from modules.calculate_num_shells import calculate_num_shells
from modules.calculate_num_access_files import calculate_num_access_files
from modules.calculate_num_outbound_cmds import calculate_num_outbound_cmds
from modules.calculate_is_host_login import calculate_is_host_login
from modules.calculate_is_guest_login import calculate_is_guest_login
from modules.calculate_count import calculate_count
from modules.calculate_srv_count import calculate_srv_count
from modules.calculate_serror_rate import calculate_serror_rate
from modules.calculate_srv_serror_rate import calculate_srv_serror_rate
from modules.calculate_rerror_rate import calculate_rerror_rate
from modules.calculate_srv_rerror_rate import calculate_srv_rerror_rate
from modules.calculate_same_srv_rate import calculate_same_srv_rate
from modules.calculate_diff_srv_rate import calculate_diff_srv_rate
from modules.calculate_srv_diff_host_rate import calculate_srv_diff_host_rate
from modules.calculate_dst_host_count import calculate_dst_host_count
from modules.calculate_dst_host_srv_count import calculate_dst_host_srv_count
from modules.calculate_dst_host_same_srv_rate import calculate_dst_host_same_srv_rate
from modules.calculate_dst_host_diff_srv_rate import calculate_dst_host_diff_srv_rate
from modules.calculate_dst_host_same_src_port_rate import calculate_dst_host_same_src_port_rate
from modules.calculate_dst_host_srv_diff_host_rate import calculate_dst_host_srv_diff_host_rate
from modules.calculate_dst_host_serror_rate import calculate_dst_host_serror_rate
from modules.calculate_dst_host_srv_serror_rate import calculate_dst_host_srv_serror_rate
from modules.calculate_dst_host_rerror_rate import calculate_dst_host_rerror_rate
from modules.calculate_dst_host_srv_rerror_rate import calculate_dst_host_srv_rerror_rate
from scapy.all import *
import dpkt

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
        'wrong_fragment' : calculate_wrong_fragment(packet),
        'urgent' : calculate_urgent(packet),
        'is_host_login' : calculate_is_host_login(packet),
        'is_guest_login' : calculate_is_guest_login(packet),
        'num_shells' : calculate_num_shells(packet),
        'num_outbound_cmds' : calculate_num_outbound_cmds(packet),
    }
    processed_packets.append(processed_packet)




features = ['hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_access_files', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']
for feature in features:
    with open(pcap_file, 'rb') as pcap_filee:
        pcap = dpkt.pcap.Reader(pcap_filee)
        # Calculate the feature by calling the appropriate function and passing the pcap file and append features to each dictionary in processed_packets
        for i in range(len(processed_packets)):
            processed_packets[i][feature] = globals()[f'calculate_{feature}'](pcap)


# Print the processed packets
print(processed_packets)