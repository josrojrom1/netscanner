###########
# IMPORTS #
from scapy.all import ARP, Ether, srp
import os
os.system('clear')
##########
# Banner #
with open('banner.txt', 'r') as b:
    for line in b:
        print(line.strip().replace('#', ''))
########################################################
# Función principal para escanear hosts en nuestra red #
def scan_ips(ip_range):
    arp = ARP(pdst=ip_range) # Paquete ARP con IP a escanear
    ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Paquete Ethernet enviado a dirección de difusión
    packet = ether/arp # Se conbinan ambos paquetes 
    result = srp(packet, timeout=3, verbose=2)[0] # Se envía el paquete a la red
    devices = [] # Lista vacía que almacenará las ips y macs que se encuentren
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.1.0/24"  # Cambia esto por tu rango de IP
    devices = scan_ips(ip_range)
    print('---------------------------------------------')
    print("Dispositivos en la red:")
    print('---------------------------------------------')
    for device in devices:
        print(f"(*) IP: {device['ip']} - MAC: {device['mac']}")
        print('---------------------------------------------\n')