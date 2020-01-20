import socket

website = str(input("Enter the host to be scanned: "))
ip = socket.gethostbyname(website)

print (ip)

while True:
	port = int(input("Enter the port: "))
	
	try:
		sock = socket.socket()			
		test = sock.connect((ip, port))
		print ("Port {}: Open" .format(port))
		sock.close()
	except:
		print ("Port {}: Closed" .format(port))
	
print ("Port Scanning complete")