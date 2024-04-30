###########
# IMPORTS #
from scapy.all import ARP, Ether, srp
import os
import sys
import re
##########
# Colors #
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_ORANGE = "\033[38;5;208m"
RESET_COLOR = "\033[0m"
##############
# CHECK SUDO #
if os.geteuid() != 0:
    print(f"\nThis script requires administrator privileges ({COLOR_ORANGE}sudo{RESET_COLOR}) to run correctly.")
    print(f"Please {COLOR_GREEN}rerun{RESET_COLOR} the script with {COLOR_ORANGE}sudo{RESET_COLOR}.\n")
    sys.exit(1)
##########
# Banner #
os.system('clear')
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
        try:
        # IP range
            ip_range = input("Insert IP range or private network (Example: 192.168.1.0/24): ")
        except KeyboardInterrupt:
            print("\n\n")
            print(f"   {COLOR_YELLOW}> Ctrl+c pressed. Exiting... <{RESET_COLOR}\n\n")
            sys.exit(0)

        
        if ip_range_pattern.search(ip_range.strip()):
            print("\n")
            print(f"   {COLOR_GREEN}> {ip_range} is a valid IP range! <{RESET_COLOR}\n")
            break
        else:
            # Using ANSI scape sequences to aply log colors
            print("\n")
            print(f"   {COLOR_RED}> Invalid argument '{ip_range}', please try again! <{RESET_COLOR}\n\n")
            #print("\n")
    print("\n")
    devices = scan_ips(ip_range)
    print('---------------------------------------------')
    print("Dispositivos en la red:")
    print('---------------------------------------------')
    for device in devices:
        if ip_gateway.search(device['ip']):
            print(f"(*) IP: {device['ip']} - MAC: {device['mac']}  {COLOR_ORANGE}> Gateway <{RESET_COLOR}")
            print('---------------------------------------------')
        else:
            print(f"(*) IP: {device['ip']} - MAC: {device['mac']}  {COLOR_GREEN}> Host <{RESET_COLOR}")
            print('---------------------------------------------')
    print("\n")