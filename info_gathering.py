import socket
import whois
import dns.resolver
import shodan
import requests
import argparse

argparse = argparse.ArgumentParser(description="This is a basic information gathering tool.", usage="python3 info_gathering.py -d DOMAIN [-s I]")
argparse.add_argument("-d","--domain",help="Enter the domain name for footprinting.",required=True)
argparse.add_argument("-s","--shodan",help="Enter the IP for shodan search.")
argparse.add_argument("-o","--output",help="Enter the Output File Path.")


args = argparse.parse_args()
domain = args.domain
ip = args.shodan
output = args.output


print("[+] Domain {} and IP {}".format(domain, ip))

#whois module
print("[+] Getting whois info..")
whois_result ='' #TO get the result in particular file path
# using whois library, creating instance
try:

    py = whois.query(domain)
    print("[+] whois info found.")
    whois_result += "Name: {}".format(py.name) + '\n'
    whois_result += "Registrar: {}".format(py.registrar) + '\n'
    whois_result += "Creation Date: {}".format(py.creation_date) + '\n'
    whois_result += "Expiration Date: {}".format(py.expiration_date) + '\n'
    whois_result += "Registrant: {}".format(py.registrar) + '\n'
    whois_result += "Registrant Country: {}".format(py.registrar_country) + '\n'
except:
    pass
print(whois_result)

#DNS module
print("[+] Getting DNS info..")
dns_result = ''
#implementing dns.resolver from dnspython

try:
    for a in dns.resolver.resolve(domain,'A'):
        dns_result += ("[+] A Record: {}".format(a.to_text())) + '\n'
    for ns in dns.resolver.resolve(domain,'NS'):
        dns_result += ("[+] NS Record: {}".format(ns.to_text())) + '\n'
    for mx in dns.resolver.resolve(domain, 'MX'):
        dns_result += ("[+] MX Record: {}".format(mx.to_text())) + '\n'
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_result += ("[+] TXT Record: {}".format(txt.to_text())) + '\n'
except:
    pass
print(dns_result)
#Geolocation Module

print("[+] Getting geolocation info..")
geo_result = ''
#implementing request for web request
try:
    response = requests.request('GET', "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    geo_result +=("[+] Country: {}".format(response['country_name'])) + '\n'
    geo_result +=("[+] Latitude: {}".format(response['latitude'])) + '\n'
    geo_result +=("[+] Longitude: {}".format(response['longitude'])) + '\n'
    geo_result +=("[+] City: {}".format(response['city'])) + '\n'
    geo_result +=("[+] State: {}".format(response['state'])) + '\n'
except:
    pass
print(geo_result)

if ip:
    #shodan API
    shodan_result = ''
    print("[+] Getting info from Shodan for IP {}".format(ip))
    api = shodan.Shodan("")
    try:
        results = api.search(ip)
        shodan_result +=("[+] Results found: {}".format(results['total']))
        for result in results['matches']:
        #As there is lots of information so to get the particular fields we use this
            shodan_result +=("[+] IP: {}".format(result['ip_str']))
            shodan_result +=("[+] Data: \n{}".format(result['data']))
            print() #just for new line

    except:
        shodan_result +=("[-] Shodan search error.")
        pass
    print(shodan_result)



if output:
    with open(output, 'w') as file:
        file.write(whois_result + '\n\n')
        file.write(dns_result + '\n\n')
        file.write(geo_result + '\n\n')

    if ip:
        shodan_output = "shodan_results.txt"  # File path for storing Shodan results
        with open(shodan_output, 'w') as shodan_file:
            shodan_file.write(shodan_result + '\n\n')
