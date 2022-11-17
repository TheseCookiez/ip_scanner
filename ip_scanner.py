import concurrent.futures
import os

ip_addresses = []
usr_input = str(input("[+] Enter the IP range you want to scan (i.e 192.168.1.0)\n"))
subnet = usr_input.rsplit('.',1)[0]
print(f"Scanning all IPs in subnet {subnet}.0-255")
for i in range(0,255):
	ip_addresses.append(f"{subnet}.{i}")

def ping(ip):
	response = os.system(f"ping -t2 -c1 {ip} >/dev/null")
	if response == 0:
		print(f"{ip} is up!")
	else:
		print(f"{ip} is not responding...")

def main():
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(ping, ip_addresses)

if __name__ == '__main__':
	main()