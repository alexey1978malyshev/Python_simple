import nmap
import csv
from os import path

# Создаем объект сканера
nm = nmap.PortScanner()

# Сканируем хост
nm.scan('127.0.0.1', '22-443')

# Выводим результаты
# print(nm.all_hosts(),  nm.scaninfo())
#
#
# print(nm['127.0.0.1'].hostname())
with open('scan_res.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(nm.scaninfo().items(), )
    csv_writer.writerow(['Host', 'Port', 'State'])  # Заголовки
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                csv_writer.writerow([host, port, state])

#print(nm.csv())