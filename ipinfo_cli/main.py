import os
import sys
import json
import argparse
import colorama
import requests
from cryptography.fernet import Fernet

class Scraper:
    def __init__(self):
        self.url = "https://ipinfo.io/"
        self.key_file = "key.key"
        self.token_file = "token.txt"
        self._generate_key()
    
    def _generate_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as keyfile:
                keyfile.write(key)
    
    def _load_key(self):
        with open(self.key_file, 'rb') as keyfile:
            return keyfile.read()
    
    def save_token(self, token):
        key = self._load_key()
        f = Fernet(key)
        encrypted_token = f.encrypt(token.encode())
        with open(self.token_file, "wb") as file:
            file.write(encrypted_token)
        print(f"Token saved to {os.path.abspath(self.token_file)} successfully.")
    
    def _decrypt_token(self):
        key = self._load_key()
        f = Fernet(key)
        with open(self.token_file, 'rb') as file:
            encrypted_token = file.read()
        decrypted_token = f.decrypt(encrypted_token).decode()
        return decrypted_token
    
    def delete_token(self):
        if os.path.exists(self.token_file):
            os.remove(self.token_file)
            os.remove(self.key_file)
            print("Token deleted successfully.")
        else:
            print("No token found.")
    
    def save_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        path = os.path.abspath("ipinfo.json")
        print(f"Data saved to {path} successfully.")
    
    def get_ip_info(self, ip_address):
        headers = {}
        if os.path.exists(self.token_file):
            token = self._decrypt_token()
            r = requests.get(self.url + ip_address + "/json" + "?token=" + token, headers=headers)
            if r.status_code == 200:
                return r.json()
            else:
                print(f"Error fetching IP informaiton. Status Code: {r.status_code}")
                return None
        else:
            r = requests.get(self.url + ip_address + "/json", headers=headers)
            if r.status_code == 200:
                return r.json()
            else:
                print(f"Error fetching IP informaiton. Status Code: {r.status_code}")
                return None

class c:
    RED = colorama.Fore.RED
    BLUE = colorama.Fore.BLUE
    YELLOW = colorama.Fore.YELLOW
    GREEN = colorama.Fore.GREEN
    CYAN = colorama.Fore.CYAN
    MAGENTA = colorama.Fore.MAGENTA
    BLACK = colorama.Fore.BLACK
    RESET = colorama.Style.RESET_ALL

def main():
    parser = argparse.ArgumentParser(description="Get information about an IP address")
    parser.add_argument("--ip", help="The IP address to look up")
    parser.add_argument("--json", help="Save the output to a JSON file")
    parser.add_argument("--token", help="Save your ipinfo.io token to a file")
    parser.add_argument("--delete-token", action="store_true", help="Delete your ipinfo.io token file")
    args = parser.parse_args()
    tools = Scraper()
    
    if args.token:
        tools.save_token(args.token)
    
    if args.delete_token:
        tools.delete_token()
    
    if args.ip:
        try:
            ip_info = json.dumps(tools.get_ip_info(args.ip), indent=4)
            
            if ip_info is not None:
                ip_info = json.loads(ip_info)
                ip = ip_info.get("ip", "N/A")
                if ip != "N/A":
                    print(f"{c.GREEN}IP Address: {c.RESET}{ip}")
                
                city = ip_info.get("city", "N/A")
                if city != "N/A":
                    print(f"{c.GREEN}City: {c.RESET}{city}")
                
                region = ip_info.get("region", "N/A")
                if region != "N/A":
                    print(f"{c.GREEN}Region: {c.RESET}{region}")
                
                country = ip_info.get("country", "N/A")
                if country != "N/A":
                    print(f"{c.GREEN}Country: {c.RESET}{country}")
                
                location = ip_info.get("loc", "N/A")
                if location != "N/A":
                    print(f"{c.GREEN}Location: {c.RESET}{location}")
                
                postal = ip_info.get("postal", "N/A")
                if postal != "N/A":
                    print(f"{c.GREEN}Postal: {c.RESET}{postal}")
                
                timezone = ip_info.get("timezone", "N/A")
                if timezone != "N/A":
                    print(f"{c.GREEN}Timezone: {c.RESET}{timezone}")
                
                asn = ip_info.get("asn", {})
                asn_number = asn.get("asn", "N/A")
                if asn_number != "N/A":
                    print(f"{c.GREEN}ASN Number: {c.RESET}{asn_number}")
                
                asn_name = asn.get("name", "N/A")
                if asn_name != "N/A":
                    print(f"{c.GREEN}ASN Name: {c.RESET}{asn_name}")
                
                asn_domain = asn.get("domain", "N/A")
                if asn_domain != "N/A":
                    print(f"{c.GREEN}ASN Domain: {c.RESET}{asn_domain}")
                
                asn_route = asn.get("route", "N/A")
                if asn_route != "N/A":
                    print(f"{c.GREEN}ASN Route: {c.RESET}{asn_route}")
                
                asn_type = asn.get("type", "N/A")
                if asn_type != "N/A":
                    print(f"{c.GREEN}ASN Type: {c.RESET}{asn_type}")
                
                company = ip_info.get("company", {})
                company_name = company.get("name", "N/A")
                if company_name != "N/A":
                    print(f"{c.GREEN}Company Name: {c.RESET}{company_name}")
                
                company_domain = company.get("domain", "N/A")
                if company_domain != "N/A":
                    print(f"{c.GREEN}Company Domain: {c.RESET}{company_domain}")
                
                company_type = company.get("type", "N/A")
                if company_type != "N/A":
                    print(f"{c.GREEN}Company Type: {c.RESET}{company_type}")
                
                privacy = ip_info.get("privacy", {})
                privacy_vpn = privacy.get("vpn", "N/A")
                if privacy_vpn != "N/A":
                    print(f"{c.GREEN}VPN: {c.RESET}{privacy_vpn}")
                
                privacy_proxy = privacy.get("proxy", "N/A")
                if privacy_proxy != "N/A":
                    print(f"{c.GREEN}Proxy: {c.RESET}{privacy_proxy}")
                
                privacy_tor = privacy.get("tor", "N/A")
                if privacy_tor != "N/A":
                    print(f"{c.GREEN}Tor: {c.RESET}{privacy_tor}")
                
                privacy_hosting = privacy.get("hosting", "N/A")
                if privacy_hosting != "N/A":
                    print(f"{c.GREEN}Hosting: {c.RESET}{privacy_hosting}")
                
                privacy_service = privacy.get("service", "N/A")
                if privacy_service != "N/A":
                    print(f"{c.GREEN}Service: {c.RESET}{privacy_service}")
                
                abuse = ip_info.get("abuse", {})
                abuse_address = abuse.get("address", "N/A")
                if abuse_address != "N/A":
                    print(f"{c.GREEN}Abuse Address: {c.RESET}{abuse_address}")
                
                abuse_country = abuse.get("country", "N/A")
                if abuse_country != "N/A":
                    print(f"{c.GREEN}Abuse Country: {c.RESET}{abuse_country}")
                
                abuse_email = abuse.get("email", "N/A")
                if abuse_email != "N/A":
                    print(f"{c.GREEN}Abuse Email: {c.RESET}{abuse_email}")
                
                abuse_name = abuse.get("name", "N/A")
                if abuse_name != "N/A":
                    print(f"{c.GREEN}Abuse Name: {c.RESET}{abuse_name}")
                
                abuse_network = abuse.get("network", "N/A")
                if abuse_network != "N/A":
                    print(f"{c.GREEN}Abuse Network: {c.RESET}{abuse_network}")
                
                abuse_phone = abuse.get("phone", "N/A")
                if abuse_phone != "N/A":
                    print(f"{c.GREEN}Abuse Phone: {c.RESET}{abuse_phone}")
                
                domains = ip_info.get("domains", {})
                domains_page = ip_info.get("page", "N/A")
                if domains_page != "N/A":
                    print(f"{c.GREEN}Domains Page: {c.RESET}{domains_page}")
                
                domains_total = ip_info.get("total", "N/A")
                if domains_total != "N/A":
                    print(f"{c.GREEN}Domains Total: {c.RESET}{domains_total}")
                
                domains_domains = domains.get("domains", "N/A")
                if domains_domains != "N/A":
                    print(f"{c.GREEN}Domains: {c.RESET}{domains_domains}")
                
                if args.json:
                    tools.save_json(args.json, ip_info)
            else:
                print(f"{c.RED}Could not get information for IP address: {args.ip}{c.RESET}")
                sys.exit(1)
        except Exception as e:
            print(f"{c.RED}An unexpected error has occurred: {e}{c.RESET}")
            sys.exit(1)
    

if __name__ == "__main__":
    main()