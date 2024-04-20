import dpkt
import socket
import collections

from scapy.utils import rdpcap

import calculate_count
import calculate_diff_srv_rate
import calculate_dst_host_count
import calculate_dst_host_diff_srv_rate
import calculate_dst_host_rerror_rate
import calculate_dst_host_same_src_port_rate
import calculate_dst_host_same_srv_rate
import calculate_dst_host_serror_rate
import calculate_dst_host_srv_count
import calculate_dst_host_srv_diff_host_rate
import calculate_dst_host_srv_rerror_rate
import calculate_dst_host_srv_serror_rate
import calculate_is_guest_login
import calculate_is_host_login
import calculate_num_outbound_cmds
import calculate_num_shells
import calculate_rerror_rate
import calculate_same_srv_rate
import calculate_serror_rate
import calculate_srv_count
import calculate_srv_diff_host_rate
import calculate_srv_serror_rate
import calculate_srv_rerror_rate


def main(pcap_file):
    # Open pcap file
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)

        # Calculate attributes
        count = calculate_count.calculate_count(pcap)
        diff_srv_rate = calculate_diff_srv_rate.calculate_diff_srv_rate(pcap)
        dst_host_count = calculate_dst_host_count.calculate_dst_host_count(pcap)
        dst_host_diff_srv_rate = calculate_dst_host_diff_srv_rate.calculate_dst_host_diff_srv_rate(pcap)
        dst_host_rerror_rate = calculate_dst_host_rerror_rate.calculate_dst_host_rerror_rate(pcap)
        dst_host_same_src_port_rate = calculate_dst_host_same_src_port_rate.calculate_dst_host_same_src_port_rate(pcap)
        dst_host_same_srv_rate = calculate_dst_host_same_srv_rate.calculate_dst_host_same_srv_rate(pcap)
        dst_host_serror_rate = calculate_dst_host_serror_rate.calculate_dst_host_serror_rate(pcap)
        dst_host_srv_count = calculate_dst_host_srv_count.calculate_dst_host_srv_count(pcap)
        dst_host_srv_diff_host_rate = calculate_dst_host_srv_diff_host_rate.calculate_dst_host_srv_diff_host_rate(pcap)
        dst_host_srv_rerror_rate = calculate_dst_host_srv_rerror_rate.calculate_dst_host_srv_rerror_rate(pcap)
        dst_host_srv_serror_rate = calculate_dst_host_srv_serror_rate.calculate_dst_host_srv_serror_rate(pcap)
        is_guest_login = calculate_is_guest_login.calculate_is_guest_login(pcap)
        is_host_login = calculate_is_host_login.calculate_is_host_login(pcap)
        num_outbound_cmds = calculate_num_outbound_cmds.calculate_num_outbound_cmds(pcap)
        num_shells = calculate_num_shells.calculate_num_shells(pcap)
        rerror_rate = calculate_rerror_rate.calculate_rerror_rate(pcap)
        same_srv_rate = calculate_same_srv_rate.calculate_same_srv_rate(pcap)
        serror_rate = calculate_serror_rate.calculate_serror_rate(pcap)
        srv_count = calculate_srv_count.calculate_srv_count(pcap)
        srv_diff_host_rate = calculate_srv_diff_host_rate.calculate_srv_diff_host_rate(pcap)
        srv_serror_rate = calculate_srv_serror_rate.calculate_srv_serror_rate(pcap)
        srv_rerror_rate = calculate_srv_rerror_rate.calculate_srv_rerror_rate(pcap)

    # Print results
    print("Count:", count)
    print("Diff_srv_rate:", diff_srv_rate)
    print("Dst_host_count:", dst_host_count)
    print("Dst_host_diff_srv_rate:", dst_host_diff_srv_rate)
    print("Dst_host_rerror_rate:", dst_host_rerror_rate)
    print("Dst_host_same_src_port_rate:", dst_host_same_src_port_rate)
    print("Dst_host_same_srv_rate:", dst_host_same_srv_rate)
    print("Dst_host_serror_rate:", dst_host_serror_rate)
    print("Dst_host_srv_count:", dst_host_srv_count)
    print("Dst_host_srv_diff_host_rate:", dst_host_srv_diff_host_rate)
    print("Dst_host_srv_rerror_rate:", dst_host_srv_rerror_rate)
    print("Dst_host_srv_serror_rate:", dst_host_srv_serror_rate)
    print("Is_guest_login:", is_guest_login)
    print("Is_host_login:", is_host_login)
    print("Num_outbound_cmds:", num_outbound_cmds)
    print("Num_shells:", num_shells)
    print("Rerror_rate:", rerror_rate)
    print("Same_srv_rate:", same_srv_rate)
    print("Serror_rate:", serror_rate)
    print("Srv_count:", srv_count)
    print("Srv_diff_host_rate:", srv_diff_host_rate)
    print("Srv_serror_rate:", srv_serror_rate)
    print("Srv_rerror_rate:", srv_rerror_rate)


pcap_file = input("Enter the path to the pcap file: ")
main(pcap_file)