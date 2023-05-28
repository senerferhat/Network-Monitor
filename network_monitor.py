from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from ping3 import ping, verbose_ping
import time
import argparse
import socket
import threading

def threaded_port_scanning(ip, start_port=1, end_port=1024):
    result = []
    threads = []

    def scan(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((ip, port)) == 0:
            result.append(port)
        sock.close()

    for port in range(start_port, end_port+1):
        thread = threading.Thread(target=scan, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if result:
        return f'Open ports on {ip}:\n' + '\n'.join(map(str, result))
    else:
        return f'No open ports found on {ip}.'


def perform_ping(ip):
    result = ""
    if ping(ip) is not None:
        result = f'The host {ip} is reachable.'
    else:
        result = f'The host {ip} is unreachable.'
    return result

def measure_latency(ip):
    latencies = []
    for _ in range(10):
        latencies.append(ping(ip))
        time.sleep(1)
    min_latency = f'RTT Min: {min(latencies):.2f} ms'
    max_latency = f'RTT Max: {max(latencies):.2f} ms'
    avg_latency = f'RTT Avg: {sum(latencies)/len(latencies):.2f} ms'
    return f"{min_latency}\n{max_latency}\n{avg_latency}"

def perform_traceroute(target, max_hops=30, timeout=2):
    result = f'Traceroute to {target}:\n'
    
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=timeout, verbose=0)
        
        if reply is None:
            result += f'{ttl} hops away: Request timed out\n'
        elif reply[ICMP].type == 11 and reply[ICMP].code == 0:
            result += f'{ttl} hops away: {reply.src}\n'
        else:
            result += f'Destination reached at {ttl} hops: {reply.src}\n'
            break

    return result

def port_scanning(ip, start_port=1, end_port=1024):
    result = f'Open ports on {ip}:\n'
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((ip, port)) == 0:
            result += f'{port}\n'
        sock.close()
    return result

def dns_lookup(host):
    try:
        ip = socket.gethostbyname(host)
        return f'The IP address of {host} is {ip}'
    except socket.gaierror:
        return f'Unable to get IP address of {host}'

def threaded_port_scanning(ip, start_port=1, end_port=1024):
    result = []
    threads = []

    def scan(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((ip, port)) == 0:
            result.append(port)
        sock.close()

    for port in range(start_port, end_port+1):
        thread = threading.Thread(target=scan, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if result:
        return f'Open ports on {ip}:\n' + '\n'.join(map(str, result))
    else:
        return f'No open ports found on {ip}.'
     
def main():
    parser = argparse.ArgumentParser(description='Network Monitoring Tool')
    parser.add_argument('-p', '--ping', help='Perform ICMP Echo Request')
    parser.add_argument('-l', '--latency', help='Measure RTT')
    parser.add_argument('-t', '--traceroute', help='Perform Traceroute')
    args = parser.parse_args()

    if args.ping:
        perform_ping(args.ping)
    elif args.latency:
        measure_latency(args.latency)
    elif args.traceroute:
        perform_traceroute(args.traceroute)

if __name__ == "__main__":
    main()
