import subprocess, os, re, threading, argparse
from colorama import Fore, init, Style

print("")
init(autoreset=True)
so = os.name ; user=os.getlogin()
parser = argparse.ArgumentParser(description='Ping a un rango de direcciones IP en la red')
parser.add_argument('-a', '--address', type=str, help='Dirección IP (como 192.168.1.2)')
args = parser.parse_args()
user_ip = args.address
if user_ip is None:
 parser.print_help()
 exit(1)

ip = '.'.join(user_ip.split('.')[:-1]) + '.'
found = []
ttl = []
lock = threading.Lock()

def ping(direccion_ip):
 if so == 'nt':
  command = f'ping -w 2 -n 3 {direccion_ip}'
 else:
  command = f'ping -W 2 -c 3 {direccion_ip}'
 process = subprocess.run(command, stdout=subprocess.PIPE, text=True)
 salida = process.stdout
 buscar = re.search(r'TTL=(\d+)', salida, re.IGNORECASE)
 if not buscar:
  with lock:
   print(f"{Fore.RED}{Style.BRIGHT}<=> Error <=> {Fore.WHITE}({direccion_ip})")
 else:
  ttl_value = buscar.group(1)
  with lock:
   print(f"{Fore.GREEN}{Style.BRIGHT}<=> Found <=> {Fore.WHITE}({direccion_ip}) TTL={ttl_value}")
   ttl.append(ttl_value)
   found.append(direccion_ip)

threads = []
for i in range(0, 256):
 direccion_ip = f"{ip}{i}"
 if direccion_ip != user_ip:
  thread = threading.Thread(target=ping, args=(direccion_ip,))
  threads.append(thread)
  thread.start()

for thread in threads:
 thread.join()

n = 1
if len(found) > 0:
 print("\n <=== Direcciones IP Conectadas a tu RED ===> \n")
 for a, b in zip(found, ttl):
  if int(b) > 100:
   print(f"---> [{n}] {Fore.GREEN}{Style.BRIGHT}{a} (TTL={b}) --> {Fore.WHITE}Posible OS [Windows]")
  else:
   print(f"---> [{n}] {Fore.GREEN}{Style.BRIGHT}{a} (TTL={b}) --> {Fore.WHITE}Posible OS/Kernel [Linux]")
  n += 1
