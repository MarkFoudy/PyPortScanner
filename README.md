# PyPortScanner

PyPortScanner is a command line tool designed to enhance the capabilities of a port scanner. It allows you to reliably scan and enumerate open ports on target computers. This tool supports scanning both TCP and UDP ports.

# Objectives and Justification

The main goal of this project was to create a functional and reliable port scanner that can be used to evaluate open ports on hosts in any network. Due to the limited timeframe for completing this project, certain design choices were made. This project builds upon the work done in a previous assignment (Assignment 4.2) and aims to enhance the functionality of the script. Instead of using an Object-Oriented Programming (OOP) approach, a structured programming approach was chosen, taking advantage of Python's multi-paradigm nature. Python's extensive library of modules makes it a popular choice among cybersecurity professionals, network engineers, and data scientists.


# Roadblocks encountered adding the UDP scan functionality

The primary roadblock encountered during the development of this program was getting the UDP scanner to function correctly. UDP (User Datagram Protocol) differs significantly from TCP (Transmission Control Protocol). TCP is a connection-oriented protocol with error correction and proof of reception. In a port scanner, receiving a response from the target is sufficient to log open TCP ports. Additionally, Python's Berkeley Socket API simplifies socket creation for TCP scanning.

UDP, on the other hand, is a connectionless protocol without mechanisms for error checking or guaranteed delivery of packets. When a UDP port is open, the target computer often responds by passing the UDP connection attempt to the application layer. Unlike TCP, a UDP port is considered open when it doesn't respond to a transmission attempt. Developing a UDP scanner required accounting for datagram loss and implementing retransmission to ensure delivery. Finding Python UDP scanners as references proved challenging, especially ones using a structured programming approach. Fortunately, a solution provided by Dr. Sierra allowed for the UDP scan to function correctly. With this assistance, focus shifted to adding additional functionality to the Python script and implementing suggestions from the Final Project Specification.

# Additional Functionality

One of the key accomplishments of this project is the ability to provide port information to the user. The scanner offers options to print the port information to the console after each scan or store it in a text file. To enable this feature, two JSON files were created to hold UDP and TCP port information. Saving port information directly using Python's print function resulted in unexpected characters appearing in the output. As a workaround, a write function was included after each print statement, allowing the port information to be displayed on the command line and written to a file if specified by the user.

Note: This README file describes the PyPortScanner project, its objectives, roadblocks encountered, and additional functionality implemented. For detailed instructions on how to use the tool, please refer to the documentation or comments within the source code. PyPortScanner is a port scanner written in Python which can be used to scan both TCP and UDP ports.  

# Installation

To clone the PyPortScanner project and run it on your local machine, follow these steps:

```git
git clone https://github.com/MarkFoudy/PyPortScanner.git
```
This command downloads the PyPortScanner project to your current directory.

Navigate to the Project Directory: Once the cloning process is complete, navigate to the project directory with:

## Usage

# Options

# Usage of PyPortScanner:
 -'H' allows the user to specify either an IP address or a domain name of a target to be scanned
```bash
./pyportscan -H 172.17.0.2
```
-'f' allows the user to provide a text file list of IP addresses or domain names to be scanned in series.
```bash
./pyportscan -f IPlist.txt
```
-‘p’ allows user to provide a comma-separated list of ports to be scanned.
```bash
./pyportscan -p 20-23,80,135-139,386
```
‘-u’ allows the script to run only a UDP scan on specific ports selected by user
```bash
./pyportscan -u 22,53
```
‘-t’ allows the script to run only a TCP scan on specific ports selected by user.
```bash
./pyportscan -t 1000-2000
```
‘o’ allows the user to specify a filename where output scan data can be stored and viewed after execution.
```bash
./pyportscan -o output.txt
```
Each of these options can be used together or in combination with others:
```bash
./pyportscan -f IPlist.txt -p 20-23,80,135-139,386 -o output.txt
```

## Contributing

If you're interested in contributing to the PyPortScanner project, please take a moment to review the contributing guidelines. This might include steps for submitting pull requests, reporting bugs, or requesting new features.

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
