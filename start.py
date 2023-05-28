from tkinter import *
from network_monitor import perform_ping, measure_latency, perform_traceroute, threaded_port_scanning, dns_lookup

def execute_ping():
    ip = entry_ping.get()
    result = perform_ping(ip)
    text_output.insert(END, f'Ping to {ip}:\n{result}\n\n')

def execute_latency():
    ip = entry_latency.get()
    result = measure_latency(ip)
    text_output.insert(END, f'Latency to {ip}:\n{result}\n\n')

def execute_traceroute():
    ip = entry_traceroute.get()
    result = perform_traceroute(ip)
    text_output.insert(END, f'Traceroute to {ip}:\n{result}\n\n')

def execute_port_scanning():
    ip = entry_port_scanning.get()
    result = threaded_port_scanning(ip,)
    text_output.insert(END, f'Port Scanning {ip}:\n{result}\n\n')

def execute_dns_lookup():
    host = entry_dns_lookup.get()
    result = dns_lookup(host)
    text_output.insert(END, f'DNS Lookup for {host}:\n{result}\n\n')

window = Tk()
window.title("Network Monitoring Tool")
window.config(bg='lightblue')

pad_x = 10
pad_y = 5

label_ping = Label(window, text="IP to ping:", bg='lightblue')
label_ping.grid(row=0, column=0, padx=pad_x, pady=pad_y)
entry_ping = Entry(window)
entry_ping.grid(row=0, column=1, padx=pad_x, pady=pad_y)
button_ping = Button(window, text="Ping", command=execute_ping)
button_ping.grid(row=0, column=2, padx=pad_x, pady=pad_y)

label_latency = Label(window, text="IP to measure latency:", bg='lightblue')
label_latency.grid(row=1, column=0, padx=pad_x, pady=pad_y)
entry_latency = Entry(window)
entry_latency.grid(row=1, column=1, padx=pad_x, pady=pad_y)
button_latency = Button(window, text="Measure Latency", command=execute_latency)
button_latency.grid(row=1, column=2, padx=pad_x, pady=pad_y)

label_traceroute = Label(window, text="IP to traceroute:", bg='lightblue')
label_traceroute.grid(row=2, column=0, padx=pad_x, pady=pad_y)
entry_traceroute = Entry(window)
entry_traceroute.grid(row=2, column=1, padx=pad_x, pady=pad_y)
button_traceroute = Button(window, text="Traceroute", command=execute_traceroute)
button_traceroute.grid(row=2, column=2, padx=pad_x, pady=pad_y)

label_port_scanning = Label(window, text="IP for Port Scanning:", bg='lightblue')
label_port_scanning.grid(row=3, column=0, padx=pad_x, pady=pad_y)
entry_port_scanning = Entry(window)
entry_port_scanning.grid(row=3, column=1, padx=pad_x, pady=pad_y)
button_port_scanning = Button(window, text="Port Scan", command=execute_port_scanning)
button_port_scanning.grid(row=3, column=2, padx=pad_x, pady=pad_y)

label_dns_lookup = Label(window, text="Hostname for DNS Lookup:", bg='lightblue')
label_dns_lookup.grid(row=4, column=0, padx=pad_x, pady=pad_y)
entry_dns_lookup = Entry(window)
entry_dns_lookup.grid(row=4, column=1, padx=pad_x, pady=pad_y)
button_dns_lookup = Button(window, text="DNS Lookup", command=execute_dns_lookup)
button_dns_lookup.grid(row=4, column=2, padx=pad_x, pady=pad_y)

text_output = Text(window, height=10, width=50)
text_output.grid(row=5, column=0, columnspan=3, padx=pad_x, pady=pad_y)

window.mainloop()

