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
pcap_file = 'C:\\Users\\HP\\Desktop\\Doss_Partage\\pcap.pcap'
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
        'is_guest_login' : calculate_is_guest_login(packet)
    }
    processed_packets.append(processed_packet)

with open(pcap_file, 'rb') as pcap_filee:
    pcap = dpkt.pcap.Reader(pcap_filee)


    hot = calculate_hot(pcap)
    num_failed_logins = calculate_num_failed_logins(pcap)
    logged_in = calculate_logged_in(pcap)
    num_compromised = calculate_num_compromised(pcap)
    root_shell = calculate_root_shell(pcap)
    su_attempted = calculate_su_attempted(pcap)
    num_root = calculate_num_root(pcap)
    num_file_creations = calculate_num_file_creations(pcap)
    num_shells = calculate_num_shells(pcap)
    num_access_files = calculate_num_access_files(pcap)
    num_outbound_cmds = calculate_num_outbound_cmds(pcap)

    count = calculate_count(pcap)
    srv_count = calculate_srv_count(pcap)
    serror_rate = calculate_serror_rate(pcap)
    srv_serror_rate = calculate_srv_serror_rate(pcap)
    rerror_rate = calculate_rerror_rate(pcap)
    srv_rerror_rate = calculate_srv_rerror_rate(pcap)
    same_srv_rate = calculate_same_srv_rate(pcap)
    diff_srv_rate = calculate_diff_srv_rate(pcap)
    srv_diff_host_rate = calculate_srv_diff_host_rate(pcap)
    dst_host_count = calculate_dst_host_count(pcap)
    dst_host_srv_count = calculate_dst_host_srv_count(pcap)
    dst_host_same_srv_rate = calculate_dst_host_same_srv_rate(pcap)
    dst_host_diff_srv_rate = calculate_dst_host_diff_srv_rate(pcap)
    dst_host_same_src_port_rate = calculate_dst_host_same_src_port_rate(pcap)
    dst_host_srv_diff_host_rate = calculate_dst_host_srv_diff_host_rate(pcap)
    dst_host_serror_rate = calculate_dst_host_serror_rate(pcap)
    dst_host_srv_serror_rate = calculate_dst_host_srv_serror_rate(pcap)
    dst_host_rerror_rate = calculate_dst_host_rerror_rate(pcap)
    dst_host_srv_rerror_rate = calculate_dst_host_srv_rerror_rate(pcap)

# Append the calculated values to each dictionary in processed_packets
for packet_dict in processed_packets:
    #packet_dict['wrong_fragment'] = wrong_fragment
    #packet_dict['urgent'] = urgent
    packet_dict['hot'] = hot
    packet_dict['num_failed_logins'] = num_failed_logins
    packet_dict['logged_in'] = logged_in
    packet_dict['num_compromised'] = num_compromised
    packet_dict['root_shell'] = root_shell
    packet_dict['su_attempted'] = su_attempted
    packet_dict['num_root'] = num_root
    packet_dict['num_file_creations'] = num_file_creations
    packet_dict['num_shells'] = num_shells
    packet_dict['num_access_files'] = num_access_files
    packet_dict['num_outbound_cmds'] = num_outbound_cmds
    #packet_dict['is_host_login'] = is_host_login
    #packet_dict['is_guest_login'] = is_guest_login
    packet_dict['count'] = count
    packet_dict['srv_count'] = srv_count
    packet_dict['serror_rate'] = serror_rate
    packet_dict['srv_serror_rate'] = srv_serror_rate
    packet_dict['rerror_rate'] = rerror_rate
    packet_dict['srv_rerror_rate'] = srv_rerror_rate
    packet_dict['same_srv_rate'] = same_srv_rate
    packet_dict['diff_srv_rate'] = diff_srv_rate
    packet_dict['srv_diff_host_rate'] = srv_diff_host_rate
    packet_dict['dst_host_count'] = dst_host_count
    packet_dict['dst_host_srv_count'] = dst_host_srv_count
    packet_dict['dst_host_same_srv_rate'] = dst_host_same_srv_rate
    packet_dict['dst_host_diff_srv_rate'] = dst_host_diff_srv_rate
    packet_dict['dst_host_same_src_port_rate'] = dst_host_same_src_port_rate
    packet_dict['dst_host_srv_diff_host_rate'] = dst_host_srv_diff_host_rate
    packet_dict['dst_host_serror_rate'] = dst_host_serror_rate
    packet_dict['dst_host_srv_serror_rate'] = dst_host_srv_serror_rate
    packet_dict['dst_host_rerror_rate'] = dst_host_rerror_rate
    packet_dict['dst_host_srv_rerror_rate'] = dst_host_srv_rerror_rate

print(processed_packets)