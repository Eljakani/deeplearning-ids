from dpkt.pcap import Reader

from modules import calculate_count


pcap_file = 'C:\\Users\\HP\\Desktop\\Doss_Partage\\pcap.pcap'
with open(pcap_file, 'rb') as f:
    pcap = Reader(f)
    count = calculate_count.calculate_count(pcap)

print(count)
