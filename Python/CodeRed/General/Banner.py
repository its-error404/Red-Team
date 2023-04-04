import socket, threading, argparse

def connection(targetip,targetport):
    
    try:
        newsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        newsocket.socket((targetip,targetport))
        
        newsocket.send("Banner Query\r\n")
        results = newsocket.recv(100)
        print("{}/TCP is open".format(targetport))
        print("{}".format(str(results)))
        
    except OSError:
        print("{}/TCP is closed".format(targetport))
        
    finally:
        newsocket.close()
        

def port_scan(target, targetport):
    
    try:
        targetip = socket.gethostbyname(target)
        print("Scan Results for {}".format(targetip))
        connection(targetip,targetport)
        
    except OSError:
        print("Cannot resolve {}. Unknown Host ! ".format(targetip))
        return
    
    t = threading.Thread(target=connection, args=(target,int(port_list)))
    

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
        
        
        