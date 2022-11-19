import concurrent.futures
import os
import sys
import socket

argv = sys.argv
ip_addresses = []


def scan_current_subnet():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	subnet = ip.rsplit('.',1)[0]
	print(f"[+] Created IP list of {subnet}.0-255")
	for i in range(0,255):
		ip_addresses.append(f"{subnet}.{i}")
	main()

def user_defiend_subnet():
	usr_input = str(input("[+] Enter the IP range you want to scan (i.e 192.168.1.0)\n"))
	subnet = usr_input.rsplit('.',1)[0]
	print(f"[+] Created IP list of {subnet}.0-255")
	for i in range(0,255):
		ip_addresses.append(f"{subnet}.{i}")
	main()

def ping(ip):
	response = os.system(f"ping -t2 -c1 {ip} >/dev/null")
	if response == 0:
		print(f"{ip} is up!")
	else:
		print(f"{ip} is not responding...")

def main():
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(ping, ip_addresses)


if len(argv) < 2:
	print("""
		No argument was given, printing help (-h)

		-h		Display this help message
		-a		Scan all IPs in current subnet
		-s		Scan spcific subnet (i.e 192.168.1.0)

		""")
	exit()
elif argv[1] == "-h":
	print("""
		Printing help (-h)

		-h		Display this help message
		-a		Scan all IPs in current subnet
		-s		Scan spcific subnet (i.e 192.168.1.0)

		""")
	exit()
elif argv[1] == "-a":
	print("[+] Getting current subnet...")
	scan_current_subnet()
elif argv[1] == "-s":
	user_defiend_subnet()
