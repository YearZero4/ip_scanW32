from colorama import init, Fore, Style
from pythonping import ping
import os, threading, sys
connected_devices=[]
init(autoreset=True)
GREEN=f"{Fore.GREEN}{Style.BRIGHT}"
RED=f"{Fore.RED}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"

def tarea(gateway, inicio, fin):
 for n in range(inicio, fin):
  ip=".".join(gateway.split(".")[:-1]) + '.' + str(n)
  response = ping(ip, count=1, timeout=1)
  if response.success():   
   if ip == gateway1 or ip == gateway2:
    print(f" {GREEN}[+]{WHITE} -> {GREEN}[gateway]{WHITE} -> ", ip)
   else:
    print(f" {GREEN}[+]{WHITE} -> {GREEN}[Conectado]{WHITE} -> ", ip)
    connected_devices.append("")

def scan(gateway):
 print(f" {GREEN}[*]{WHITE} Busqueda en el rango {GREEN}{".".join(gateway.split(".")[:-1])}.1/24")
 for i in range(0, 256, 8):
  hiloA = threading.Thread(target=tarea, args=(gateway, i, i+8))
  hilos1.append(hiloA)
  hiloA.start()
 for hilo in hilos1:
  hilo.join()
 print(f"{GREEN} (" + str(len(connected_devices)) + f"){WHITE}", "dispositivos conectados ...")
 connected_devices.clear()

def error():
 print(f"{GREEN} [*] {WHITE}Para ejecutar el programa\n {GREEN}{sys.argv[0]} -a [GATEWAY] escaneo profundo \n {GREEN}{sys.argv[0]} -l [GATEWAY] escaneo rapido")

if __name__ == "__main__":
 try:
  hilos1 = [] ; hilos2=[]
  gateway1 = "192.168.0.1"
  if len(sys.argv) == 3:
   gateway2=sys.argv[2]
   if sys.argv[1] == "-a":
    scan(gateway1)
    scan(gateway2)
   elif sys.argv[1] == "-l":
    scan(gateway2)
   else:
    print(f" [-] Error argumentos invalidos...")
    error()
   
  else:
   error()
  
 except KeyboardInterrupt:
  print("\nInterrumpido...")