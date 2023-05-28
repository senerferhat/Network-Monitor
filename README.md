# Network Monitoring Tool

This is a network monitoring tool written in Python. It offers various network diagnostic features such as Ping, Traceroute, Port Scanning, and DNS Lookup, and latency measurement.

## Features

1. **Host Discovery**: Determines whether a host is online or not.
2. **Latency Measurement**: Measures the Round Trip Time (RTT) to a given host.
3. **Traceroute**: Determines the route taken by packets across a network.
4. **Port Scanning**: Checks for open ports on a given host.
5. **DNS Lookup**: Retrieves the IP address associated with a given hostname.

## Installation

Ensure that you have Python installed on your machine. Clone this repository to your local machine:

git clone https://github.com/senerferhat/Network-Monitor.git

Install the necessary Python libraries:

pip install -r requirements.txt


## Usage

You can run the GUI version of this tool by running `gui.py` or use it from the command line by running `network_monitor.py`.

### GUI Usage

Run the following command:
python gui.py

### Command Line Usage

Run `network_monitor.py` with one of the following arguments:

python network_monitor.py -p [ip_address] # Perform ICMP Echo Request
python network_monitor.py -l [ip_address] # Measure RTT
python network_monitor.py -t [ip_address] # Perform Traceroute


## Dependencies

This project depends on the following Python libraries:

- Scapy
- socket
- argparse
- threading
- tkinter
- ping3

## License

This project is licensed under the terms of the MIT license.

## Contact

If you have any questions, feel free to open an issue or submit a pull request.
