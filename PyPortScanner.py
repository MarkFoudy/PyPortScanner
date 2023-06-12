#!/usr/bin/env python3
"""
	Mark Foudy
	December 7, 2022
	Python TCP/UDP Port Scanner
	This program scans both UDP and TCP ports on targets selected by user.
"""
import json
import optparse
import sys
from socket import *
from threading import *

tcpDict={}
udpDict={}

def tcpConnScan(tgtHost, tgtPort, outfile, writeToFile):
	"""
	Function -- tcpConnScan
		This function acts as the main driver for the TCP scan functionality of the port scanner.
	Parameters:
		tgtHost -- Host address
		tgtPort -- Port address
		outfile -- file to write
		writeToFile -- bool concerning which ports should be written to file.
	Returns: a list of open or closed TCP ports.
	"""
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		result = connSkt.connect_ex((tgtHost,tgtPort))
		if result == 0:
			print ('\033[0:32;1m'"[+] %d/TCP Open" % tgtPort)
			print('\033[m')
			if writeToFile:
				outfile.write("[+] %d/TCP Open"%tgtPort)
				outfile.write("\n")
				outfile.write("\n")

			if str(tgtPort) in tcpDict:
				print("Port:",str(tgtPort),tcpDict[str(tgtPort)])
				print ('\033[m')
				if writeToFile:
					outfile.write("Port: " + str(tgtPort) + " " + tcpDict[str(tgtPort)])
					outfile.write("\n")
					outfile.write("\n")


		else:
			print ('\033[0:31;1m'"[-] %d/TCP Closed" % tgtPort)
			print ('\033[m')
			if writeToFile:
				outfile.write("[-] %d/TCP Closed"%tgtPort)
				outfile.write("\n")
				outfile.write("\n")



			if str(tgtPort) in tcpDict:
				print("Port:",str(tgtPort),tcpDict[str(tgtPort)])
				print ('\033[m')
				if writeToFile:
					outfile.write("[-] %d/TCP Closed"%tgtPort)
					outfile.write("\n")
					outfile.write("\n")
					if writeToFile:
						outfile.write("Port: " + str(tgtPort) + " " + tcpDict[str(tgtPort)])
						outfile.write("\n")
						outfile.write("\n")

	finally:
		connSkt.close()
		return result


def udpConnScan(tgtHost,tgtPort,outfile,writeToFile):
	"""
	Function -- udpConnScan
		This is the UDP scanner which is called from the command line.
	Parameters:
		tgtHost -- Host to scan
		tgtPort -- Ports to scan
		outfile -- file to write
		writeToFile -- bool concerning which ports should be written to file.
	Returns: a list of open or closed UDP ports.
	"""
	result = -1

	try:

		connSkt=socket(AF_INET,SOCK_DGRAM)
		result = connSkt.connect_ex(tgtHost,tgtPort)

	except:
		result = -1

	else:
		if result == 0:
			try:
				msg = b"" # send udp packet no data

				connSkt.sendto(msg(tgtHost,tgtPort))
			except:
				# send message fail, so port can't be open for udp
				result = -1
			else:
				try:
					data, addr = connSkt.recvfrom(1024)

				except Exception as ex:
					# Check the error type returned
					exec_type, exec_value, exec_tb = sys.exc_info()

					# we expect ConnectionRefusedError if the port isn't open for UDP
					# so if we get a timeout instead, presume port is open for UDP message but message isn't valid
					if str(exec_type) == "<class 'socket.timeout'>":
						result = 0
					else:
						result = -1
				else:
					# we received a response so port must be open
					result = 0

	finally:
		if result==0:
			print("\033[0:33;1m" "[+] %d/udp open" % tgtPort)
			print("\033[m")
			if writeToFile:
				outfile.write("[+] %d/udp open"%tgtPort)
				outfile.write("\n")
				outfile.write("\n")

			if str(tgtPort) in udpDict:
				print("Port:",str(tgtPort),udpDict[str(tgtPort)])
				print('\033[m')
				if writeToFile:
					outfile.write("Port: " + str(tgtPort) + " " + udpDict[str(tgtPort)])
					outfile.write("\n")
					outfile.write("\n")

		else:
			print("\033[0:31;1m" "[-] %d/udp closed" % tgtPort)
			print("\033[m")
			if writeToFile:
				outfile.write("[+] %d/udp closed"%tgtPort)
				outfile.write("\n")
				outfile.write("\n")
			if str(tgtPort) in udpDict:
				print("Port:",str(tgtPort),udpDict[str(tgtPort)])
				print('\033[m')
				if writeToFile:
					outfile.write("Port: " + str(tgtPort) + " " + udpDict[str(tgtPort)])
					outfile.write("\n")
					outfile.write("\n")
	# finally:
	# 	connSkt.close()
		return result



def portScanUDP(tgtHost,tgtPort,outfile,writeToFile):
	"""
	Function -- portScanUDP
		This function initiates the UDP scan of ports by calling udpConnScan.
	Parameters:
		tgtHost -- Host to be scanned
		tgtPort -- Ports to scan
		outfile -- file to write
		writeToFile -- bool concerning which ports should be written to file.
	"""
	for port in tgtPort:
		t=Thread(target=udpConnScan,args=(tgtHost,int(port),outfile,writeToFile))
		t.start()


def portScanTCP(tgtHost,tgtPort,outfile,writeToFile):
	"""
	Function -- portScanTCP
		This function scans the list of ports using the function tcpConnScan.
	Parameters:
			tgtHost -- Hosts to be scanned.
			tgtPort -- Ports to be scanned
			outfile -- file to write
			writeToFile -- bool concerning which ports should be written to file
	Returns a
	"""
	for port in tgtPort:
			t=Thread(target=tcpConnScan,args=(tgtHost,int(port),outfile,writeToFile))
			t.start()


def portScan(tgtHost,allPorts,udpPorts,tcpPorts,outfile,writeToFile):
	"""
	Function -- portScan
		This function is the main port scanner driver which is used to call both the
		portScanTCP and portScanUDP.
	Parameters:
		tgtHost -- Hosts to be scanned
		tgtPorts -- Ports to be scanned
		udpPorts -- udpPorts to be scanned
		tcpPorts -- tcpPorts to be scanned
		outfile --  file to write
		writeToFile -- bool concerning which ports should be written to file
	Returns a
	"""
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		if writeToFile:
			outfile.write("[-] Cannot resolve '%s': Unknown host" % tgtHost)
		print ("[-] Cannot resolve '%s': Unknown host" % tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		if writeToFile:
			outfile.write("\n[+] Scan Results for: " + tgtName[0])
		print ("\n[+] Scan Results for: " + tgtName[0])
	except:
		print ('\n[+] Scan Results for: ' + tgtIP)

	setdefaulttimeout(1)

	if writeToFile:
		outfile.write("[-] Hostname '%s': "%tgtHost)
		outfile.write("\n")

	if tcpPorts[0] != 'None':
		portScanTCP(tgtHost,tcpPorts,outfile,writeToFile)

	if udpPorts[0] != 'None':
		portScanUDP(tgtHost,udpPorts,outfile,writeToFile)

	if allPorts[0] != 'None':
		portScanUDP(tgtHost,allPorts,outfile,writeToFile)
		portScanTCP(tgtHost,allPorts,outfile,writeToFile)


def readIPsFromFile(fileToScan,IPList):
	"""
	Function -- readIPsFromFile
		This function reads a file containing a list of IPs and creates a list of IPs for to be scanned.
	Parameters:
		fileToScan -- file containing host addresses to be scanned.
		IPList -- list containing files to be scanned by port scanner.
	Returns a list of IPs to be scanned.
	"""
	with open(fileToScan) as file:
		while (line:= file.readline().rstrip()):
			IPList.append(line)
	file.close()
	return IPList


def main():
	"""
	Function -- Main
		This function acts as the main driver for my Python Port Scanner
	Parameters: None
	Returns a list of ports clarifying which ones are open/closed and providing information concerning the most popular ones.
	"""
	global tcpDict
	global udpDict

	f=open("tcpExplain","r")
	tcpDict=json.load(f)
	f.close()
	g=open("udpExplain","r")
	udpDict=json.load(g)
	g.close()

	IPList = []
	# outfile = open("output.txt", "w")
	outfile = None
	writeToFile = False



	parser=optparse.OptionParser(
		"usage %prog " + "-H <target host> -p <target ports> | -t <target ports> | -u <target ports> -f <filename>  -o <outfileName>")
	parser.add_option("-H", dest="tgtHost",	type="string",	help="specify target host")
	parser.add_option("-t",	dest="tcpPorts",	type="string", help="option to scan TCP")
	parser.add_option("-u",	dest="udpPorts",	type="string",	help="option to scan UDP")
	parser.add_option("-p", dest="allPorts",	type="string",	help="specify target port[s] separated by comma or a range (e.g. 80 – 443)")
	parser.add_option("-f", dest="fileToScan",	type="string",	help="option to allow a file with IPs or domains to scan")
	parser.add_option("-o", dest="outfileName",	type="string",	help="option to provide a file name where the output will be stored")

	(options,args)=parser.parse_args()
	tgtHost=options.tgtHost
	allPorts=str(options.allPorts).split(",")
	tcpPorts=str(options.tcpPorts).split(",")
	udpPorts=str(options.udpPorts).split(",")
	fileToScan=str(options.fileToScan)
	outfileName=str(options.outfileName)

	# if the user used the -o and gave a filename, then we can open it for writing
	if (outfileName != None):
		outfile = open(outfileName, "w")
		writeToFile = True
		# sys.stdout = open(outfileName, "w")

	if (tgtHost==None and fileToScan==None) or (allPorts[0]==None and tcpPorts[0]==None and udpPorts[0]==None):
		print(parser.usage)
		exit(0)


	if tgtHost!=None:
		portScan(tgtHost,allPorts,udpPorts,tcpPorts,outfile,writeToFile)
	elif fileToScan!=None:
		readIPsFromFile(fileToScan,IPList)
		for ip in IPList:
			portScan(ip,allPorts,udpPorts,tcpPorts,outfile,writeToFile)

	else:
		print(parser.usage)
		exit(0)
if __name__ == '__main__':
	main()