###########
# IMPORTS #
from scapy.all import ARP, Ether, srp
import os
import re

os.system('clear')
##########
# Banner #
with open('banner.txt', 'r') as b:
    for line in b:
        print(line.strip().replace('#', ''))
########################################################
# Principal function for scanning hosts in our network #
def scan_ips(ip_range):
    arp = ARP(pdst=ip_range) # ARP packet with IP range to be scanned
    ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Ethernet packet to be sended to difusion address
    packet = ether/arp # Combination of packets 
    result = srp(packet, timeout=3, verbose=2)[0] # Sending packet to the network
    devices = [] # Empty list for devices data (ip and mac)
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("\n")
    return devices

if __name__ == "__main__":
    # IP range pattern
    ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    ip_gateway = re.compile("^(?:[0-9]{1,3}\.){3}[1]*$")
    
    while True:
        # IP range
        ip_range = input("Insert IP range or private network (Example: 192.168.1.0/24): ")
        print("\n")
        if ip_range_pattern.search(ip_range.strip()):
            print(f"   \033[92m> {ip_range} is a valid IP range! <\033[0m")
            break
        else:
            # Using ANSI scape sequences to aply log colors
            print(f"   \033[91m> Invalid argument '{ip_range}', please try again! <\033[0m")
            print("\n")
    print("\n")
    devices = scan_ips(ip_range)
    print('---------------------------------------------')
    print("Dispositivos en la red:")
    print('---------------------------------------------')
    for device in devices:
        if ip_gateway.search(device['ip']):
            print(f"(*) IP: {device['ip']} - MAC: {device['mac']}  \033[38;5;208m> Gateway <\033[0m")
            print('---------------------------------------------')
        else:
            print(f"(*) IP: {device['ip']} - MAC: {device['mac']}  \033[92m> Host <\033[0m")
            print('---------------------------------------------')
    print("\n")