from scapy.all import *

request = ARP(pdst="10.210.16.0/28")

broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

client = srp(broadcast / request, timeout = 1)[0]

for element in client:
	print(element[1].psrc + "   " + element[1].hwsrc)

#print(request.summary())


