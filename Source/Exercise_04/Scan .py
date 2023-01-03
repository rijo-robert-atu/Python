# finding the addresses and port number in the list

scan = {"192.168.3.10":"80","192.168.3.11":"443","192.168.3.55":"22"}
for ipv4,port in scan.items():
# finding the service from the list
	print(f"Found a serice on {ipv4} at {port}")