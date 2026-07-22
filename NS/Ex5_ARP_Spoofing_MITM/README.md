# Lab Experiment 5: ARP Attack and MITM Demonstration

## 1. Aim
To implement and demonstrate Address Resolution Protocol (ARP) spoofing and how it can be used to launch a Man-in-the-Middle (MITM) attack in a controlled lab environment.

## 2. Algorithm
1. **Network Setup**: Identify the IP address of the victim machine and the IP of the gateway/router.
2. **Craft ARP Packets**: Create fake ARP reply packets to poison the victim’s ARP cache by associating the attacker’s MAC address with the gateway’s IP.
3. **Send ARP Spoof Packets**: Continuously send these spoofed ARP replies to the victim and the gateway, making both think the attacker is the other party.
4. **MITM Attack**: Once the ARP cache is poisoned, all traffic between victim and gateway flows through the attacker machine. The attacker can capture, modify, or drop packets.
5. **Restore ARP Table**: After the experiment, send correct ARP packets to restore the normal communication and prevent disruption.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> **Case 1: Before Attack**
> * Victim’s ARP table:
>   `192.168.1.1` &rarr; `00:11:22:33:44:55` (real gateway MAC)
>
> **Case 2: During Attack**
> * Victim’s ARP table after spoofing:
>   `192.168.1.1` &rarr; `00:0c:29:aa:bb:cc` (attacker’s MAC)
> * Gateway’s ARP table is also poisoned to map victim’s IP to attacker’s MAC.
> * All traffic between victim and gateway passes through attacker.
>
> **Case 3: After Attack**
> * ARP tables restored with real MAC addresses.
> * Normal communication resumes.

## 4. Result
The experiment successfully demonstrated how ARP spoofing can redirect network traffic through an attacker’s system, enabling a Man-in-the-Middle (MITM) attack, thereby proving the vulnerability of ARP and the risks it poses to secure communication.
