from scapy.all import *
from io import BytesIO

from scapy.layers.inet import TCP


def calculate_urgent(packet):
    urgent_count = 0

    if packet.haslayer(TCP) and packet.getlayer(TCP).flags & 0x20:
        urgent_count += 1
    return urgent_count