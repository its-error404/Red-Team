import dns.resolver

#Specifying target and record types

target_domain = input("\nEnter the target domain:  ")
record_types=["A","AAAA","CNAME","MX","NS","SOA","TXT"]

#creating DNS resolver
dnsresolver = dns.resolver.Resolver()

for record in record_types:
    try:
        result = dnsresolver.resolve(target_domain,record)
    except:
        dns.resolver.NoAnswer

        continue
    
    print(f"\n{record} records for {target_domain}:  \n")
    for data in result:
        print(f"{data}")


