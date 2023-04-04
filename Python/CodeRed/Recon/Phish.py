import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import re

def argument_parser():
    
    parser = argparse.ArgumentParser(description="Email")
    parser.add_argument("Server", help="SMTP Server to send mail")
    parser.add_argument("Port", help="SMTP Server port")
    parser.add_argument("Username", help="Username")
    parser.add_argument("Password",help="Password")
    parser.add_argument("Email",help="Pre-crafted email location")
    parser.add_argument("URL",help="Url that will get replaced in all links in mail")
    parser.add_argument("Subject", help="subject of the mail")
    parser.add_argument("Sender",help="Email Sender")
    parser.add_argument("Sendto", help="Target Email Address")
    parser.add_argument("--tls",help="Attempt to use SSL/TLS")

    var_args = vars(parser.parse_args())
    return var_args

def open_email(email_file):
    with open(email_file, 'r') as open_email:
        email_html = open_email.read()

    return email_html

def replace_links(url,message):
    html_regex = re.compile(r'href=[\'"]?([^\'">]+)')
    html_output = html_regex.sub("href=\"{}".format(url),message)
    
    return html_output

def mime_message ( email_subj, sendto , sendfrom, html_email):
    msg = MIMEMultipart('alternative')
    msg['To'] = sendto
    msg["From"] = sendfrom
    msg['Subject']=email_subj
    message = MIMEText(html_email,'html')
    msg.attach(message)
    
    return msg.as_string()

def send_email(server,port,username,password,sendfrom,sendto,message,tls):
    print("Attempting to connect to server")
    start_server = smtplib.SMTP(server,port)
    
    if tls:
        print("Attempting to use STARTTLS")
        start_server.starttls()
    
    print("Attempting to say hello")
    start_server.login(username,password)
    print("Attempting to send mail")
    start_server.sendmail(sendfrom,sendto,message)
    print("Done")
    start_server.quit()
    
def go_phishing(server,port,username,password,email_location,url_replace,subject,sendfrom,sendto,tls):
    html_email = open_email(email_location)
    html_output = replace_links(url_replace, html_email)
    message = mime_message(subject,sendto, sendfrom, html_output)
    send_email(server,port,username,password,sender, sendto,message,tls)
    
if __name__ == '__main__':
    try:
        user_args = argument_parser()
        email_server = user_args("server")
        smtp_port = user_args("port")
        login = user_args("username")
        password = user_args("password")
        email_path = user_args("email")
        new_url = user_args("url")
        email_subject = user_args('subject')
        
        go_phishing(email_server,smtp_port,login,password,email_path,new_url,email_subject,sender,receiver,use_tls)
    
    except AttributeError:
        print("Error ! Provide arguments before running !")
        
    
    
    
                            