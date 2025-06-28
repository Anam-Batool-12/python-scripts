import whois
import socket
import dns.resolver

domain = input("Enter the domain name: ")
info = whois.whois(domain)
print("\n[WHOIS Info]")
print(info)


print("\n[IP Address]")
print(socket.gethostbyname(domain)) 

print("\n[DNS Records]")
import whois
import socket
import dns.resolver

domain = input("Enter a domain: ")


info = whois.whois(domain)
print("\n[WHOIS Info]")
print(info)


print("\n[IP Address]")
try:
    print(socket.gethostbyname(domain))
except:
    print("Could not resolve IP address.")


record_types = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT', 'SOA']

print("\n[DNS Records]")
for qtype in record_types:
    try:
        answers = dns.resolver.resolve(domain, qtype)
        print(f"\n{qtype} Records:")
        for rdata in answers:
            print(f" - {rdata.to_text()}")
    except:
        print(f"No {qtype} record found or query failed.")

for qtype in ['A', 'MX', 'NS']:
    try:
        answers = dns.resolver.resolve(domain, qtype)
        print(f"{qtype} Records:")
        for rdata in answers:
            print(f" - {rdata.to_text()}")
    except:
        print(f"No {qtype} record found.")



