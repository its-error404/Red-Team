import argparse, nmap

def argument_parser():
    
    parser = argparse.ArgumentParser(description="TCP Port Scanner. Accepts a hostname/IP and list of ports to scan. Also attempts to identiy the service running on the port")
    parser.add_argument("-t","--target",nargs="?", help="Target IP to scan")
    parser.add_argument("-p","--ports",nargs="?", help="Enter the Ports to scan. Seperate the ports with comma like 22,21")
    
    var_args = vars(parser.parse_args())
    
    return var_args


def scan(host,port):
    thescan = nmap.PortScanner()
    thescan.scan(host,port)
    
    state = thescan[host]['tcp'][int(port)]['state']
    result = (" {host} tcp/{port} {state}".format(host=host,port=port,state=state))
    
    return result


if __name__ == "__main__":
    
    try:
        userargs = argument_parser()
        host = userargs['target']
        ports = userargs['ports'].split('.')
        
        for port in ports:
            print(scan(host,ports))
    except AttributeError:
        print("Provide Args !")    