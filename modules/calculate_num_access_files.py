import dpkt
import socket

def calculate_num_access_files(pcap):
    num_access_files = 0

    for timestamp, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)

            if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                ip = eth.data
                protocol = ip.p

                if protocol == dpkt.ip.IP_PROTO_TCP:
                    tcp = ip.data
                    src_port = tcp.sport
                    dst_port = tcp.dport
                    data = tcp.data

                    if dst_port == 80 or dst_port == 8080 or dst_port == 443:
                        # HTTP, HTTP Proxy, or HTTPS traffic
                        try:
                            http = dpkt.http.Request(data)
                            if http.method == 'GET' or http.method == 'POST':
                                num_access_files += 1
                        except dpkt.NeedData:
                            pass

        except dpkt.NeedData:
            continue

    return num_access_files