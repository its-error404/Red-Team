import requests

# Target subdomain
domain = input("Enter Target Domain:  ")
# Read all subdomains from a text file
file = open('subdomains.txt')
# reading the content of the file
listofdomains = file.readlines()
discovered_subdomains = []

for subdomain in listofdomains:
    # URL Construction
    url = f"https://{subdomain}.{domain}"
    try:
        # If this raises an error, then the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered Subdomains: ",url)
        discovered_subdomains.append(url)

with open("discovered_subdomains.txt",'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)



