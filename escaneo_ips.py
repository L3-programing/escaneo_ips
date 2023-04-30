import nmap
import time
def escaneo_completo():
    ep = nmap.PortScanner()
    host = input("ip: ")  + "/24"
    argument = "-Pn -T 5 -v -PR"
    escaneado = ep.scan(hosts=host, ports="1" ,arguments=argument)
    for all_hosts in ep.all_hosts():
        if ep[all_hosts].state() == 'up':
            time.sleep(0.4)
            print("-------------------------------------")
            escaneo = all_hosts,":", ep[all_hosts].state()
            print(all_hosts,":", ep[all_hosts].state())
escaneo_completo()