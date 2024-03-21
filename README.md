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
Option 1: Download the Code Directly from GitHub

    Navigate to the Repository: Go to the GitHub page for the PyPortScanner project: PyPortScanner GitHub Repository.

    Download the Repository: Click on the Code button, then select Download ZIP.

    Extract the Files: Once the download is complete, extract the ZIP file to your desired location.

    Run the Program:
        Open a terminal or command prompt.
        Navigate to the directory where you extracted the files.
        Before running the program, ensure you have Python installed on your system. This project is likely designed to run with Python 3.x.
        Install any dependencies if listed in a requirements.txt file by running pip install -r requirements.txt.
        Execute the program by running python pyportscanner.py (replace pyportscanner.py with the correct script name if different).

Option 2: Clone the Repository Using Git

    Open a Terminal/Command Prompt: Ensure you have Git installed on your system.

    Clone the Repository:
        Run the command gh repo clone MarkFoudy/PyPortScanner to clone the repository directly using GitHub CLI, or use git clone https://github.com/MarkFoudy/PyPortScanner.git if you're not using GitHub CLI.

    Navigate to the Project Directory: cd PyPortScanner

    Install Dependencies: If there's a requirements.txt file, install the required Python packages using pip install -r requirements.txt.

    Run the Program: Execute the script with python pyportscanner.py (adjust the script name as necessary).

Just download the code and run it.
```bash
https://github.com/MarkFoudy/PyPortScanner.git
```
Or clone the repo:
```bash
gh repo clone MarkFoudy/PyPortScanner
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
