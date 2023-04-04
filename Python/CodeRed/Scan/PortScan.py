import argparse, socket, threading

def connection_scan(targetip, portnum):
    co_socket = 0
    
    try:
        co_socket == socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        co_socket.connect(targetip,portnum)
        print("{}/tcp is open".format(portnum))
        
    except OSError:
        print("{}/tcp is closed".format(portnum))
        
    finally:
        co_socket.close()
        

def port_scan(target, targetport):
    
    try:
        targetip = socket.gethostbyname(target)
        print("Scan Results for {}".format(targetip))
        connection_scan(targetip,targetport)
        
    except OSError:
        print("Cannot resolve {}. Unknown Host ! ".format(targetip))
        return
    
    t = threading.Thread(target=connection_scan, args=(target,int(port_list)))
    

def argument_parser():
    
    parser = argparse.ArgumentParser(description="TCP Port Scanner. Accepts a hostname/IP and list of ports to scan. Also attempts to identiy the service running on the port")
    parser.add_argument("-t","--target",nargs="?", help="Target IP to scan")
    parser.add_argument("-p","--ports",nargs="?", help="Enter the Ports to scan. Seperate the ports with comma like 22,21")
    
    var_args = vars(parser.parse_args())
    
    return var_args


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["target"]
        port_list = user_args["ports"].split(',')
        
        for port in port_list:
            port_scan(host,port_list)
            
    except AttributeError:
        print("Error !! Please provide command - line arguments before running")
        