from scapy.all import rdpcap

def ip_source(packet):
	if packet.haslayer('IP'):
	    source_ip = packet['IP'].src
	    return source_ip


